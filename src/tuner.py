
from typing import Optional
import PySide6.QtCore
import PySide6.QtWidgets
import pyaudio

import utils
from utils import *
from logger import logger
import ui.tuner

'''
References:
    https://github.com/TomSchimansky/GuitarTuner
'''


class Signal(QtCore.QObject):

    frame = QtCore.Signal(object)


class AudioCanvas(FigureCanvasQTAgg):

    def __init__(self, buffer_size=1024) -> None:
        super().__init__(Figure())
        self.ax = self.figure.add_subplot(1, 1, 1)
        self.line, = self.ax.plot(range(buffer_size))
        self.ax.set_ylim(-32768, 32768)
        self.ax.margins(0.01)
        # self.axes.axis('off')

        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.spines['left'].set_visible(False)

        self.ax.get_xaxis().set_ticks([])
        self.ax.get_yaxis().set_ticks([])

        self.ax.set_facecolor((0.8, 0.8, 0.8))

        # self.figure.tight_layout()
        self.figure.subplots_adjust(
            top=1,
            bottom=0,
            left=0,
            right=1,
            hspace=0,
            wspace=0,
        )

    def update_canvas(self, data):
        self.line.set_ydata(data)
        self.draw()


class Tuner(QtWidgets.QWidget):

    SAMPLING_RATE = 44100
    CHUNK_SIZE = 2048
    BUFFER_SIZE = CHUNK_SIZE * 5
    ZERO_PADDING = 3
    A0 = 27.5
    NOTENAMES = 'A A# B C C# D D# E F F# G G#'.split(" ")

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        logger.info("Tuner init...")
        self.setWindowIcon(QtGui.QIcon(FAVICON))
        self.setWindowTitle('Tuner')

        self.form = ui.tuner.Ui_Tuner()
        self.form.setupUi(self)

        self.audio_canvas = AudioCanvas(self.BUFFER_SIZE)
        self.form.buffer_layout.addWidget(self.audio_canvas)

        self.signal = Signal(self)
        self.signal.frame.connect(self.draw_frame)

        # init audio
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.SAMPLING_RATE,
            input=True,
            # output=True,
            frames_per_buffer=self.CHUNK_SIZE,
            stream_callback=self.stream_callback)
        self.stream.start_stream()
        self.buffer = np.zeros(self.BUFFER_SIZE)
        self.hanning = np.hanning(len(self.buffer))

    def closeEvent(self, event: QCloseEvent) -> None:
        logger.info("Tuner closing...")

        self.stream.stop_stream()
        self.audio.terminate()

        return super().closeEvent(event)

    def update_note(self, freq: float):
        n = 12 * np.log2(freq / self.A0)
        if n > 88 or n < 0:
            return

        cents = (n - round(n)) * 100
        self.form.cents.setText(f'{cents:.02f}')

        # logger.debug(n)

        number, note = divmod(round(n), 12)
        name = self.NOTENAMES[note]
        self.form.note.setText(name[0])
        if len(name) > 1:
            self.form.accidental.setText(name[1])
        else:
            self.form.accidental.setText(" ")
        self.form.number.setText(str(number))

        # logger.debug((note, number, name, names))

    @QtCore.Slot(object)
    def draw_frame(self, datas):
        buffer = datas[0]
        freq = datas[1]
        self.form.hertz.setText(f'{freq:04.02f}')
        self.update_note(freq)
        self.audio_canvas.update_canvas(buffer)

    def stream_callback(self, data, frame_count, time_info, status):
        # logger.debug("input stream data len %s %s", len(data), type(data))
        frame = np.frombuffer(data, np.int16)
        self.buffer[:-self.CHUNK_SIZE] = self.buffer[self.CHUNK_SIZE:]
        self.buffer[-self.CHUNK_SIZE:] = frame

        sdata = self.buffer * self.hanning

        amps = np.absolute(np.fft.rfft(sdata))
        amps = amps[:int(len(amps) / 2)]

        # todo (Harmonic Product Spectrum)

        freqs = np.fft.fftfreq(int(len(amps) * 2), 1. / self.SAMPLING_RATE)

        freq = freqs[np.argmax(amps)]
        # logger.debug(freq)

        self.signal.frame.emit([self.buffer, freq])

        return (data, pyaudio.paContinue)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wnd = Tuner()
    wnd.show()
    app.exec()
