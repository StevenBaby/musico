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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QSizePolicy, QSpacerItem, QSplitter,
    QVBoxLayout, QWidget)

class Ui_Tuner(object):
    def setupUi(self, Tuner):
        if not Tuner.objectName():
            Tuner.setObjectName(u"Tuner")
        Tuner.resize(481, 728)
        self.verticalLayout_2 = QVBoxLayout(Tuner)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.buffer_layout = QVBoxLayout()
        self.buffer_layout.setObjectName(u"buffer_layout")

        self.verticalLayout_2.addLayout(self.buffer_layout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.frame = QFrame(Tuner)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.note = QLabel(self.frame)
        self.note.setObjectName(u"note")
        font = QFont()
        font.setFamilies([u"Fira Code"])
        font.setPointSize(72)
        self.note.setFont(font)
        self.note.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.note)

        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.accidental = QLabel(self.splitter)
        self.accidental.setObjectName(u"accidental")
        sizePolicy.setHeightForWidth(self.accidental.sizePolicy().hasHeightForWidth())
        self.accidental.setSizePolicy(sizePolicy)
        self.accidental.setMaximumSize(QSize(50, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Fira Code"])
        font1.setPointSize(28)
        self.accidental.setFont(font1)
        self.accidental.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.splitter.addWidget(self.accidental)
        self.number = QLabel(self.splitter)
        self.number.setObjectName(u"number")
        sizePolicy.setHeightForWidth(self.number.sizePolicy().hasHeightForWidth())
        self.number.setSizePolicy(sizePolicy)
        self.number.setMaximumSize(QSize(50, 16777215))
        self.number.setFont(font1)
        self.number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.splitter.addWidget(self.number)

        self.horizontalLayout.addWidget(self.splitter)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cents = QLabel(self.frame)
        self.cents.setObjectName(u"cents")
        sizePolicy.setHeightForWidth(self.cents.sizePolicy().hasHeightForWidth())
        self.cents.setSizePolicy(sizePolicy)
        self.cents.setMinimumSize(QSize(100, 0))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(18)
        self.cents.setFont(font2)
        self.cents.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.cents)

        self.cents_label = QLabel(self.frame)
        self.cents_label.setObjectName(u"cents_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cents_label.sizePolicy().hasHeightForWidth())
        self.cents_label.setSizePolicy(sizePolicy1)
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
        sizePolicy.setHeightForWidth(self.hertz.sizePolicy().hasHeightForWidth())
        self.hertz.setSizePolicy(sizePolicy)
        self.hertz.setMinimumSize(QSize(100, 0))
        self.hertz.setFont(font2)
        self.hertz.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.hertz)

        self.hertz_label = QLabel(self.frame)
        self.hertz_label.setObjectName(u"hertz_label")
        sizePolicy1.setHeightForWidth(self.hertz_label.sizePolicy().hasHeightForWidth())
        self.hertz_label.setSizePolicy(sizePolicy1)
        self.hertz_label.setFont(font3)

        self.horizontalLayout_2.addWidget(self.hertz_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Tuner)

        QMetaObject.connectSlotsByName(Tuner)
    # setupUi

    def retranslateUi(self, Tuner):
        Tuner.setWindowTitle(QCoreApplication.translate("Tuner", u"Tuner", None))
        self.note.setText(QCoreApplication.translate("Tuner", u"A", None))
        self.accidental.setText(QCoreApplication.translate("Tuner", u"#", None))
        self.number.setText(QCoreApplication.translate("Tuner", u"4", None))
        self.cents.setText(QCoreApplication.translate("Tuner", u"0000.00", None))
        self.cents_label.setText(QCoreApplication.translate("Tuner", u"Ct", None))
        self.hertz.setText(QCoreApplication.translate("Tuner", u"0000.00", None))
        self.hertz_label.setText(QCoreApplication.translate("Tuner", u"Hz", None))
    # retranslateUi

