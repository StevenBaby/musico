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


class MPLCanvas(FigureCanvasQTAgg):

    def __init__(self) -> None:
        self.figure = Figure()
        super().__init__(self.figure)
        self.axes = self.figure.add_subplot(1, 1, 1)
        self.axes.margins(0.01)

        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)

        self.axes.get_xaxis().set_ticks([])
        self.axes.get_yaxis().set_ticks([])

        self.axes.set_facecolor((0.8, 0.8, 0.8))

        # self.figure.tight_layout()
        self.figure.subplots_adjust(
            top=1,
            bottom=0,
            left=0,
            right=1,
            hspace=0,
            wspace=0,
        )


class AudioCanvas(MPLCanvas):

    def __init__(self, buffer_size=1024) -> None:
        super().__init__()

        self.line, = self.axes.plot(range(buffer_size), color=utils.COLOR)
        self.axes.set_ylim(-32768, 32768)

        # self.axes.axis('off')

    def update_data(self, data: np.ndarray):
        # data = data.copy() / data.max()
        self.line.set_ydata(data)
        self.draw()


class CentBar(MPLCanvas):

    def __init__(self) -> None:
        super().__init__()
        self.axes.set_xlim(-100.0, 100.0)
        self.bar, = self.axes.barh([1, ], width=[50], color=utils.COLOR)

    def update_data(self, data):
        self.bar.set_width(data)
        self.draw()


class Tuner(QtWidgets.QWidget):

    SAMPLING_RATE = 44100
    CHUNK_SIZE = 2048
    BUFFER_SIZE = CHUNK_SIZE * 10
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

        self.centbar = CentBar()
        self.form.centbar_layout.addWidget(self.centbar)

        self.signal = Signal(self)
        self.signal.frame.connect(self.draw_frame)

        self.form.input_devices_box.currentIndexChanged.connect(
            self.input_index_changed,
        )

        # init audio
        self.buffer = np.zeros(self.BUFFER_SIZE)
        self.hanning = np.hanning(len(self.buffer))

        self.audio = pyaudio.PyAudio()
        for i in range(0, self.audio.get_host_api_count()):
            info = self.audio.get_device_info_by_host_api_device_index(0, i)
            if info.get('maxInputChannels') == 0:
                continue
            self.form.input_devices_box.addItem(
                info.get('name'),
                userData=info
            )
            logger.info(info)

        self.restart_stream(0)

    def restart_stream(self, index):
        if hasattr(self, 'stream'):
            self.stream.stop_stream()
        self.form.input_devices_box.setCurrentIndex(index)
        info = self.form.input_devices_box.itemData(index)
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.SAMPLING_RATE,
            input=True,
            # output=True,
            frames_per_buffer=self.CHUNK_SIZE,
            stream_callback=self.stream_callback,
            input_device_index=info.get('index'),
        )
        self.stream.start_stream()

    def closeEvent(self, event: QCloseEvent) -> None:
        logger.info("Tuner closing...")

        self.stream.stop_stream()
        self.audio.terminate()

        return super().closeEvent(event)

    def input_index_changed(self, index):
        logger.debug("index changed %s", index)
        self.restart_stream(index)

    def update_note(self, freq: float):
        if freq < 27.5 or freq > 5000:
            return

        n = 12 * np.log2(freq / self.A0)
        if n > 88 or n < 0:
            return

        self.form.hertz.setText(f'{freq:04.02f}')

        cents = (n - round(n)) * 100
        self.form.cents.setText(f'{cents:.02f}')
        self.centbar.update_data(cents)

        # logger.debug(n)

        number, note = divmod(round(n), 12)
        name = self.NOTENAMES[note]
        self.form.note.setText(name[0])
        if len(name) > 1:
            self.form.accidental.setText(name[1])
        else:
            self.form.accidental.setText(" ")
        if note > 2: # start with A0 A#0 B0 C1 ...
            number += 1
        self.form.number.setText(str(number))

    @QtCore.Slot(object)
    def draw_frame(self, datas):
        buffer = datas[0]
        freq = datas[1]
        self.update_note(freq)
        self.audio_canvas.update_data(buffer)

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
    # wnd = CentBar()
    wnd.show()
    app.exec()
