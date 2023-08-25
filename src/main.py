import os
import sys

from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui,
    QtUiTools,
)

import mido


from logger import logger

dirname = os.path.dirname(os.path.abspath(__file__))
assets = os.path.abspath(os.path.join(dirname, "../assets"))


class MainWindow(QtWidgets.QMainWindow):

    def midi_input_callback(self, msg):
        logger.debug("input message %s", msg)
        self.outport.send(msg)

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


def main():
    logger.info("Musico is starting...")
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
