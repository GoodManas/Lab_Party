# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QSizePolicy,
    QTableView, QWidget)

class Ui_History(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(800, 500))
        Form.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.00568182 rgba(255, 151, 191, 255), stop:1 rgba(255, 106, 138, 255))")
        self.h_label = QLabel(Form)
        self.h_label.setObjectName(u"h_label")
        self.h_label.setGeometry(QRect(20, 10, 91, 31))
        font = QFont()
        font.setPointSize(18)
        self.h_label.setFont(font)
        self.h_label.setStyleSheet(u"background-color: rgba(85, 255, 255, 0);\n"
"color: rgb(255, 230, 255);")
        self.history_table = QTableView(Form)
        self.history_table.setObjectName(u"history_table")
        self.history_table.setGeometry(QRect(20, 50, 761, 401))
        self.history_table.setStyleSheet(u"background-color:rgb(255, 200, 255);\n"
"border: 1px solied rgb(255, 255, 255);\n"
"\n"
"color: rgb(125, 41, 62);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.h_label.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
    # retranslateUi

