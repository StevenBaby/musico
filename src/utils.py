# coding=utf-8

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

import scipy.special as scispecial

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui,
    QtUiTools,
)

from PySide6.QtGui import (
    QCloseEvent,
    QKeyEvent,
    QMouseEvent
)

DIRNAME = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.abspath(os.path.join(DIRNAME, "assets"))
FAVICON = os.path.join(ASSETS, "favicon.ico")
KEYBOARD = os.path.join(ASSETS, "keyboard.jpg")

RED = '#db2828'
PINK = '#e03997'
BLUE = '#2185d0'
ORANGE = '#f2711c'
GREEN = '#21ba45'
YELLOW = '#fbbd08'
PURPLE = '#a333c8'
