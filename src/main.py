import os
import sys

from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui,
    QtUiTools,
)


from logger import logger

dirname = os.path.dirname(os.path.abspath(__file__))
assets = os.path.abspath(os.path.join(dirname, "../assets"))

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setWindowIcon(QtGui.QIcon(os.path.join(assets, "favicon.ico")))
        self.setWindowTitle("Musico")


def main():
    logger.info("Musico is starting...")
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
