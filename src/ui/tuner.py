# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tuner.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QSizePolicy, QSpacerItem,
    QSplitter, QVBoxLayout, QWidget)

class Ui_Tuner(object):
    def setupUi(self, Tuner):
        if not Tuner.objectName():
            Tuner.setObjectName(u"Tuner")
        Tuner.resize(418, 741)
        self.verticalLayout_6 = QVBoxLayout(Tuner)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget0 = QWidget(Tuner)
        self.widget0.setObjectName(u"widget0")
        self.horizontalLayout_3 = QHBoxLayout(self.widget0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget0)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.input_api_box = QComboBox(self.widget0)
        self.input_api_box.setObjectName(u"input_api_box")

        self.horizontalLayout_3.addWidget(self.input_api_box)


        self.horizontalLayout_9.addWidget(self.widget0)

        self.widget6 = QWidget(Tuner)
        self.widget6.setObjectName(u"widget6")
        self.horizontalLayout_7 = QHBoxLayout(self.widget6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget6)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.input_devices_box = QComboBox(self.widget6)
        self.input_devices_box.setObjectName(u"input_devices_box")

        self.horizontalLayout_7.addWidget(self.input_devices_box)


        self.horizontalLayout_9.addWidget(self.widget6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.splitter = QSplitter(Tuner)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setMinimumSize(QSize(0, 200))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.buffer_layout = QVBoxLayout()
        self.buffer_layout.setObjectName(u"buffer_layout")

        self.verticalLayout_2.addLayout(self.buffer_layout)

        self.splitter.addWidget(self.widget1)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget4 = QWidget(self.layoutWidget)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setMinimumSize(QSize(0, 200))
        self.widget4.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.spectrum_layout = QVBoxLayout()
        self.spectrum_layout.setObjectName(u"spectrum_layout")

        self.verticalLayout_5.addLayout(self.spectrum_layout)


        self.verticalLayout_3.addWidget(self.widget4)

        self.widget5 = QWidget(self.layoutWidget)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setMinimumSize(QSize(0, 25))
        self.widget5.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_4 = QHBoxLayout(self.widget5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.spectrum_tick_layout = QVBoxLayout()
        self.spectrum_tick_layout.setObjectName(u"spectrum_tick_layout")

        self.horizontalLayout_4.addLayout(self.spectrum_tick_layout)


        self.verticalLayout_3.addWidget(self.widget5)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.layoutWidget1)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.note = QLabel(self.frame)
        self.note.setObjectName(u"note")
        font = QFont()
        font.setFamilies([u"Fira Code"])
        font.setPointSize(72)
        self.note.setFont(font)
        self.note.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.note)

        self.widget2 = QWidget(self.frame)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.widget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.accidental = QLabel(self.widget2)
        self.accidental.setObjectName(u"accidental")
        sizePolicy1.setHeightForWidth(self.accidental.sizePolicy().hasHeightForWidth())
        self.accidental.setSizePolicy(sizePolicy1)
        self.accidental.setMaximumSize(QSize(30, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Fira Code"])
        font1.setPointSize(28)
        self.accidental.setFont(font1)
        self.accidental.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.accidental)

        self.number = QLabel(self.widget2)
        self.number.setObjectName(u"number")
        sizePolicy1.setHeightForWidth(self.number.sizePolicy().hasHeightForWidth())
        self.number.setSizePolicy(sizePolicy1)
        self.number.setMaximumSize(QSize(30, 16777215))
        self.number.setFont(font1)
        self.number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.number)


        self.horizontalLayout.addWidget(self.widget2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.centbar_widget = QWidget(self.frame)
        self.centbar_widget.setObjectName(u"centbar_widget")
        self.centbar_widget.setMinimumSize(QSize(0, 30))
        self.centbar_widget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_5 = QHBoxLayout(self.centbar_widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centbar_layout = QVBoxLayout()
        self.centbar_layout.setSpacing(0)
        self.centbar_layout.setObjectName(u"centbar_layout")

        self.horizontalLayout_5.addLayout(self.centbar_layout)


        self.verticalLayout.addWidget(self.centbar_widget)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cents = QLabel(self.frame)
        self.cents.setObjectName(u"cents")
        sizePolicy1.setHeightForWidth(self.cents.sizePolicy().hasHeightForWidth())
        self.cents.setSizePolicy(sizePolicy1)
        self.cents.setMinimumSize(QSize(100, 0))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(18)
        self.cents.setFont(font2)
        self.cents.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.cents)

        self.cents_label = QLabel(self.frame)
        self.cents_label.setObjectName(u"cents_label")
        sizePolicy.setHeightForWidth(self.cents_label.sizePolicy().hasHeightForWidth())
        self.cents_label.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Fira Code"])
        font3.setPointSize(18)
        self.cents_label.setFont(font3)

        self.horizontalLayout_8.addWidget(self.cents_label)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.hertz = QLabel(self.frame)
        self.hertz.setObjectName(u"hertz")
        sizePolicy1.setHeightForWidth(self.hertz.sizePolicy().hasHeightForWidth())
        self.hertz.setSizePolicy(sizePolicy1)
        self.hertz.setMinimumSize(QSize(100, 0))
        self.hertz.setFont(font2)
        self.hertz.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.hertz)

        self.hertz_label = QLabel(self.frame)
        self.hertz_label.setObjectName(u"hertz_label")
        sizePolicy.setHeightForWidth(self.hertz_label.sizePolicy().hasHeightForWidth())
        self.hertz_label.setSizePolicy(sizePolicy)
        self.hertz_label.setFont(font3)

        self.horizontalLayout_2.addWidget(self.hertz_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_6.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_6.addWidget(self.splitter)


        self.retranslateUi(Tuner)

        QMetaObject.connectSlotsByName(Tuner)
    # setupUi

    def retranslateUi(self, Tuner):
        Tuner.setWindowTitle(QCoreApplication.translate("Tuner", u"Tuner", None))
        self.label_2.setText(QCoreApplication.translate("Tuner", u"Input API", None))
        self.label_3.setText(QCoreApplication.translate("Tuner", u"Input Device", None))
        self.note.setText(QCoreApplication.translate("Tuner", u"A", None))
        self.accidental.setText(QCoreApplication.translate("Tuner", u"#", None))
        self.number.setText(QCoreApplication.translate("Tuner", u"4", None))
        self.cents.setText(QCoreApplication.translate("Tuner", u"----.--", None))
        self.cents_label.setText(QCoreApplication.translate("Tuner", u"Ct", None))
        self.hertz.setText(QCoreApplication.translate("Tuner", u"----.--", None))
        self.hertz_label.setText(QCoreApplication.translate("Tuner", u"Hz", None))
    # retranslateUi

