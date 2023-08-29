
import PySide6.QtGui
from utils import *

from logger import logger


class Keyboard(QtWidgets.QLabel):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        logger.info("Keyboard init...")
        self.setWindowIcon(QtGui.QIcon(FAVICON))
        self.setWindowTitle('Keyboard')

    def keyPressEvent(self, event: QKeyEvent) -> None:
        logger.debug(event)
        return super().keyPressEvent(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        logger.debug(event)
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        logger.debug(event)
        return super().mouseMoveEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wnd = Keyboard()
    wnd.show()
    app.exec()
