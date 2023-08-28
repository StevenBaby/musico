import pyaudiowpatch as pyaudio

import utils
from utils import *
from logger import logger
import ui.tuner


class MPLCanvas(FigureCanvasQTAgg):

    def __init__(self) -> None:
        self.figure = Figure()
        super().__init__(self.figure)
        self.axes = self.figure.add_subplot(1, 1, 1)
        self.axes.margins(0.01)
        self.axes.set_facecolor((0.8, 0.8, 0.8))

        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)

        self.axes.get_xaxis().set_ticks([])
        self.axes.get_xaxis().set_ticks([], minor=True)
        self.axes.get_yaxis().set_ticks([])

        # # self.figure.tight_layout()
        self.figure.subplots_adjust(
            top=1,
            bottom=0,
            left=0,
            right=1,
            hspace=0,
            wspace=0,
        )


class AudioCanvas(MPLCanvas):

    def __init__(self) -> None:
        super().__init__()
        self.inited = False
        self.line = None
        self.axes.set_ylim(-32768, 32768)

    def update_data(self, data: np.ndarray):
        # data = data.copy() / data.max()
        if not self.inited:
            self.inited = True
            self.line, = self.axes.plot(data, color=utils.PINK)
        else:
            self.line.set_ydata(data)
        self.draw()


class SpectrumTicksCanvas(MPLCanvas):

    def __init__(self) -> None:
        super().__init__()
        self.axes.set_xlim(20, 5000)
        self.figure.subplots_adjust(
            top=1,
            bottom=0.999,
            left=0,
            right=1,
            hspace=0,
            wspace=0,
        )
        self.axes.set_xscale('log')
        self.axes.get_xaxis().set_ticks([], minor=True)

        ticks = [(27.5 * 2 ** i) for i in range(8)]
        labels = [f'$A_{i}$' for i in range(8)]
        self.axes.get_xaxis().set_ticks(ticks, labels)
        logger.info("set ticks %s", ticks)
        logger.info("set labels %s", labels)


class SpectrumCanvas(MPLCanvas):

    def __init__(self) -> None:
        super().__init__()
        self.spectrum_line = None
        self.optimized_line = None
        self.bar = None
        self.inited = False

        self.axes.set_ylim(-0.1, 1.1)
        self.axes.set_xlim(20, 5000)
        # self.figure.tight_layout()
        self.figure.subplots_adjust(
            top=1,
            bottom=0,
            left=0,
            right=1,
            hspace=0,
            wspace=0,
        )

    def update_data(self, frequencies: np.ndarray, spectrum: np.ndarray, optimized: np.ndarray, frequency: float):
        if frequency > 5000:
            return

        width = 0
        if frequency > 50:
            optimized.fill(0.0)
            width = frequency / 50

        if spectrum.max() > 0:
            spectrum /= spectrum.max()
        if optimized.max() > 0:
            optimized /= optimized.max()

        if not self.inited:
            self.inited = True
            self.spectrum_line, = self.axes.plot(frequencies, spectrum, color=utils.PINK, alpha=0.7)
            self.optimized_line, = self.axes.plot(frequencies, optimized, color=utils.BLUE, alpha=0.5)
            self.bar, = self.axes.bar(
                frequency - width / 2, height=1, width=width, color=utils.GREEN)
            self.axes.set_xscale('log')
        else:
            self.spectrum_line.set_ydata(spectrum)
            self.optimized_line.set_ydata(optimized)
            self.bar.set_x(frequency - width / 2)
            self.bar.set_width(width)

        self.draw()


class CentBar(MPLCanvas):

    def __init__(self) -> None:
        super().__init__()
        self.axes.set_xlim(-50.1, 50.1)
        self.bar, = self.axes.barh([1, ], width=[0], color=utils.PINK)

    def update_data(self, data):
        self.bar.set_width(data)
        if data < -10:
            self.bar.set_color(utils.PURPLE)
        elif data > 10:
            self.bar.set_color(utils.RED)
        else:
            self.bar.set_color(utils.GREEN)
        self.draw()


class Signal(QtCore.QObject):

    frame = QtCore.Signal(object, object, object, float)


class Tuner(QtWidgets.QWidget):

    CHUNK_SIZE = 2048
    BUFFER_SIZE = CHUNK_SIZE * 10
    HPS_HARMONICS = 3
    A0 = 27.5
    NOTENAMES = 'A A# B C C# D D# E F F# G G#'.split(" ")

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        logger.info("Tuner init...")
        self.setWindowIcon(QtGui.QIcon(FAVICON))
        self.setWindowTitle('Tuner')

        self.form = ui.tuner.Ui_Tuner()
        self.form.setupUi(self)

        self.audio_canvas = AudioCanvas()
        self.form.buffer_layout.addWidget(self.audio_canvas)

        self.spectrum_canvas = SpectrumCanvas()
        self.form.spectrum_layout.addWidget(self.spectrum_canvas)

        self.form.spectrum_tick_layout.addWidget(SpectrumTicksCanvas())

        self.centbar = CentBar()
        self.form.centbar_layout.addWidget(self.centbar)

        self.signal = Signal(self)
        self.signal.frame.connect(self.draw_frame)

        self.form.input_devices_box.currentIndexChanged.connect(self.input_device_changed)
        self.form.input_api_box.currentIndexChanged.connect(self.input_api_changed)

        # init audio
        self.sample_rate = 44100
        self.buffer = np.zeros(self.BUFFER_SIZE)
        self.hanning = np.hanning(len(self.buffer))
        self.frequencies = np.fft.fftfreq(len(self.buffer), 1. / self.sample_rate)
        self.frequencies = self.frequencies[:len(self.buffer) // 2]

        self.audio = pyaudio.PyAudio()
        for i in range(0, self.audio.get_host_api_count()):
            api = self.audio.get_host_api_info_by_index(i)
            self.form.input_api_box.addItem(api.get("name"), userData=api)
            logger.info(api)

        self.form.input_api_box.setCurrentIndex(0)
        self.form.input_devices_box.setCurrentIndex(0)

    def restart_stream(self, api, index):
        if hasattr(self, 'stream'):
            self.stream.stop_stream()
        info = self.form.input_devices_box.itemData(index)
        self.sample_rate = int(info.get("defaultSampleRate"))
        logger.info("start stream %s", info)
        try:
            self.stream = self.audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=self.sample_rate,
                input=True,
                # output=True,
                frames_per_buffer=self.CHUNK_SIZE,
                stream_callback=self.stream_callback,
                input_device_index=info.get('index'),
            )
        except OSError as e:
            logger.error(e)
            self.form.input_devices_box.setItemText(index, f"[INVALID] {info.get('name')}")
            return
        self.stream.start_stream()

    def closeEvent(self, event: QCloseEvent) -> None:
        logger.info("Tuner closing...")

        self.stream.stop_stream()
        self.audio.terminate()

        return super().closeEvent(event)

    def input_device_changed(self, index):
        # logger.debug("index changed %s", index)
        api = self.form.input_api_box.currentIndex()
        self.restart_stream(api, index)

    def input_api_changed(self, index):
        self.form.input_devices_box.clear()
        logger.debug(index)
        api = self.form.input_api_box.itemData(index)
        for i in range(api.get('deviceCount')):
            info = self.audio.get_device_info_by_host_api_device_index(index, i)
            if info.get('maxInputChannels') == 0:
                continue
            logger.info(info)
            self.form.input_devices_box.addItem(
                info.get('name'),
                userData=info
            )
        self.restart_stream(api, 0)

    def update_note(self, freq: float):
        if freq < 27.5 or freq > 5000:
            return

        n = 12 * np.log2(freq / self.A0)
        if n > 88 or n < 0:
            return

        self.form.hertz.setText(f'{freq:04.02f}')

        cents = (n - round(n)) * 100
        self.form.cents.setText(f'{cents:+.02f}')
        self.centbar.update_data(cents)

        # logger.debug(n)

        number, note = divmod(round(n), 12)
        name = self.NOTENAMES[note]
        self.form.note.setText(name[0])
        if len(name) > 1:
            self.form.accidental.setText(name[1])
        else:
            self.form.accidental.setText(" ")
        if note > 2:  # start with A0 A#0 B0 C1 ...
            number += 1
        self.form.number.setText(str(number))

    def draw_frame(self, buffer: np.ndarray, spectrum: np.ndarray, optimized: np.ndarray, frequency: float):
        self.update_note(frequency)
        self.spectrum_canvas.update_data(self.frequencies, spectrum, optimized, frequency)
        self.audio_canvas.update_data(buffer)

    def algorithm_harmonic_product_spectrum(self, buffer: np.array):

        spectrum = np.absolute(np.fft.fft(buffer))

        # shannon nyquist theorem
        spectrum = spectrum[:len(self.buffer) // 2]

        # todo (Harmonic Product Spectrum)
        # reference:
        # http://musicweb.ucsd.edu/~trsmyth/analysis/Harmonic_Product_Spectrum.html
        optimized = spectrum.copy()
        for harmonic in range(2, self.HPS_HARMONICS + 1):
            hps_len = int(np.ceil(len(spectrum) / harmonic))
            optimized[:hps_len] *= spectrum[::harmonic]

        # smooth low frequencis
        args = np.argwhere(self.frequencies < 200)[-1, 0]
        x = (np.arange(args) - args // 2) / args * 8
        optimized[:args] *= scispecial.expit(x)

        return spectrum, optimized

    def stream_callback(self, data, frame_count, time_info, status):
        # logger.debug("input stream data len %s %s", len(data), type(data))
        frame = np.frombuffer(data, np.int16)

        # References:
        # https://github.com/TomSchimansky/GuitarTuner
        self.buffer[:-self.CHUNK_SIZE] = self.buffer[self.CHUNK_SIZE:]
        self.buffer[-self.CHUNK_SIZE:] = frame

        # self.buffer[np.abs(self.buffer) < .0] = 0.0

        buffer = self.buffer * self.hanning

        spectrum, optimized = self.algorithm_harmonic_product_spectrum(buffer)

        frequency = self.frequencies[np.argmax(optimized)]

        self.signal.frame.emit(self.buffer, spectrum, optimized, frequency)

        return (data, pyaudio.paContinue)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wnd = Tuner()
    # wnd = CentBar()
    wnd.show()
    app.exec()
