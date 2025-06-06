# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(350, 200))
        font = QFont()
        font.setFamilies([u"Forte"])
        Form.setFont(font)
        Form.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.00568182 rgba(255, 151, 191, 255), stop:1 rgba(255, 106, 138, 255))")
        self.user_acc = QLabel(Form)
        self.user_acc.setObjectName(u"user_acc")
        self.user_acc.setGeometry(QRect(270, 10, 71, 16))
        font1 = QFont()
        font1.setPointSize(12)
        self.user_acc.setFont(font1)
        self.user_acc.setStyleSheet(u"background-color: rgba(85, 255, 255, 0);\n"
"color: rgb(255, 230, 255);")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 179, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.layoutWidget)
        self.logo.setObjectName(u"logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Vladimir Script"])
        font2.setPointSize(30)
        self.logo.setFont(font2)
        self.logo.setLayoutDirection(Qt.LeftToRight)
        self.logo.setStyleSheet(u"background-color: rgba(85, 255, 255, 0);\n"
"color: rgb(255, 230, 255);")

        self.verticalLayout.addWidget(self.logo)

        self.available_rooms = QPushButton(self.layoutWidget)
        self.available_rooms.setObjectName(u"available_rooms")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.available_rooms.sizePolicy().hasHeightForWidth())
        self.available_rooms.setSizePolicy(sizePolicy2)
        self.available_rooms.setStyleSheet(u"background-color:rgb(255, 200, 255);\n"
"border: 1px solied rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(125, 41, 62);")

        self.verticalLayout.addWidget(self.available_rooms)

        self.history = QPushButton(self.layoutWidget)
        self.history.setObjectName(u"history")
        sizePolicy2.setHeightForWidth(self.history.sizePolicy().hasHeightForWidth())
        self.history.setSizePolicy(sizePolicy2)
        self.history.setStyleSheet(u"background-color:rgb(255, 200, 255);\n"
"border: 1px solied rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(125, 41, 62);")

        self.verticalLayout.addWidget(self.history)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.user_acc.setText(QCoreApplication.translate("Form", u"username", None))
        self.logo.setText(QCoreApplication.translate("Form", u"RanBooking", None))
        self.available_rooms.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u0438 \u0440\u0435\u0441\u0443\u0440\u0441\u044b", None))
        self.history.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0439", None))
    # retranslateUi

