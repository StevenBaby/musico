import os
import sys

from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui,
    QtUiTools,
)

from PySide6.QtGui import (
    QCloseEvent,
)

import mido
import pyaudio
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


from logger import logger

dirname = os.path.dirname(os.path.abspath(__file__))
assets = os.path.abspath(os.path.join(dirname, "../assets"))


class MainWindow(QtWidgets.QMainWindow):

    def midi_input_callback(self, msg):
        logger.debug("input message %s", msg)
        self.outport.send(msg)

    def stream_callback(self, data, frame_count, time_info, status):
        # logger.debug("input stream data len %s %s", len(data), type(data))

        # get and convert the data to float
        audio_data = np.frombuffer(data, np.int16)

        # Fast Fourier Transform, 10*log10(abs) is to scale it to dB
        # and make sure it's not imaginary
        dfft = 10. * np.log10(abs(np.fft.rfft(audio_data)))

        if not self.lines:
            line, = self.axes[0].plot(audio_data)
            self.lines.append(line)
            line, = self.axes[1].plot(dfft)
            self.lines.append(line)
        else:
            self.lines[0].set_ydata(audio_data)

            self.lines[1].set_ydata(dfft)

        self.figure.canvas.draw()

        return (data, pyaudio.paContinue)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setWindowIcon(QtGui.QIcon(os.path.join(assets, "favicon.ico")))
        self.setWindowTitle("Musico")

        logger.debug("output")
        for name in mido.get_output_names():
            logger.debug(name)

        logger.debug("input")
        for name in mido.get_input_names():
            logger.debug(name)

        # self.inport = mido.open_input(callback=self.midi_input_callback)
        # self.outport = mido.open_output()

        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            rate=44100,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            output=True,
            frames_per_buffer=4096,
            stream_callback=self.stream_callback,
        )
        self.stream.start_stream()

        self.figure = Figure()
        self.axes = self.figure.subplots(2)

        self.lines = []

        # self.axes[0].set_xlim(0, 1000)
        self.axes[0].set_ylim(-32768, 32768)
        self.axes[0].set_title("Raw Audio Signal")

        # self.axes[1].set_xlim(27.5, 4186)
        self.axes[1].set_ylim(-100, 100)
        self.axes[1].set_xscale('log')
        self.axes[1].set_title("Fast Fourier Transform")

        self.canvas = FigureCanvasQTAgg(self.figure)
        self.setCentralWidget(self.canvas)

    def closeEvent(self, event: QCloseEvent) -> None:
        logger.info("Musico is closing...")
        # self.inport.close()
        # self.outport.close()
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        return super().closeEvent(event)


def main():
    logger.info("Musico is starting...")
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
