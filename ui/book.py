# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_Book(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 500)
        Form.setMinimumSize(QSize(800, 500))
        Form.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.00568182 rgba(255, 151, 191, 255), stop:1 rgba(255, 106, 138, 255))")
        self.label_w_name = QLabel(Form)
        self.label_w_name.setObjectName(u"label_w_name")
        self.label_w_name.setGeometry(QRect(20, 20, 331, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_w_name.setFont(font)
        self.label_w_name.setStyleSheet(u"background-color: rgba(85, 255, 255, 0);\n"
"color: rgb(255, 230, 255);")
        self.info_table = QTableView(Form)
        self.info_table.setObjectName(u"info_table")
        self.info_table.setGeometry(QRect(20, 60, 761, 391))
        self.info_table.setStyleSheet(u"background-color:rgb(255, 200, 255);\n"
"border: 1px solied rgb(255, 255, 255);\n"
"color: rgb(125, 41, 62);")
        self.button_book = QPushButton(Form)
        self.button_book.setObjectName(u"button_book")
        self.button_book.setGeometry(QRect(600, 460, 177, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_book.sizePolicy().hasHeightForWidth())
        self.button_book.setSizePolicy(sizePolicy)
        self.button_book.setStyleSheet(u"background-color:rgb(255, 200, 255);\n"
"border: 1px solied rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(125, 41, 62);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0411\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label_w_name.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u0438 \u0440\u0435\u0441\u0443\u0440\u0441\u044b", None))
        self.button_book.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

