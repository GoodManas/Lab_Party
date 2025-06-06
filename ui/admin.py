# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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

class Ui_Admin(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 350)
        Form.setMinimumSize(QSize(500, 350))
        Form.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.00568182 rgba(255, 151, 191, 255), stop:1 rgba(255, 106, 138, 255))")
        self.label_z_name = QLabel(Form)
        self.label_z_name.setObjectName(u"label_z_name")
        self.label_z_name.setGeometry(QRect(10, 20, 91, 21))
        font = QFont()
        font.setPointSize(18)
        self.label_z_name.setFont(font)
        self.label_z_name.setStyleSheet(u"background-color: rgba(85, 255, 255, 0);\n"
"color: rgb(255, 230, 255);")
        self.zayavki_table = QTableView(Form)
        self.zayavki_table.setObjectName(u"zayavki_table")
        self.zayavki_table.setGeometry(QRect(10, 50, 261, 291))
        self.zayavki_table.setStyleSheet(u"background-color:rgb(255, 200, 255);\n"
"border: 1px solied rgb(255, 255, 255);\n"
"\n"
"color: rgb(125, 41, 62);")
        self.otklon_button = QPushButton(Form)
        self.otklon_button.setObjectName(u"otklon_button")
        self.otklon_button.setGeometry(QRect(290, 50, 177, 49))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otklon_button.sizePolicy().hasHeightForWidth())
        self.otklon_button.setSizePolicy(sizePolicy)
        self.otklon_button.setStyleSheet(u"background-color:rgb(255, 200, 255);\n"
"border: 1px solied rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(125, 41, 62);")
        self.accept_button = QPushButton(Form)
        self.accept_button.setObjectName(u"accept_button")
        self.accept_button.setGeometry(QRect(290, 110, 177, 49))
        sizePolicy.setHeightForWidth(self.accept_button.sizePolicy().hasHeightForWidth())
        self.accept_button.setSizePolicy(sizePolicy)
        self.accept_button.setStyleSheet(u"background-color:rgb(255, 200, 255);\n"
"border: 1px solied rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(125, 41, 62);")
        self.logotype = QLabel(Form)
        self.logotype.setObjectName(u"logotype")
        self.logotype.setGeometry(QRect(310, 210, 161, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logotype.sizePolicy().hasHeightForWidth())
        self.logotype.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Vladimir Script"])
        font1.setPointSize(70)
        self.logotype.setFont(font1)
        self.logotype.setLayoutDirection(Qt.LeftToRight)
        self.logotype.setStyleSheet(u"background-color: rgba(85, 255, 255, 0);\n"
"color: rgb(255, 230, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_z_name.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u044f\u0432\u043a\u0438", None))
        self.otklon_button.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u043b\u043e\u043d\u0438\u0442\u044c", None))
        self.accept_button.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.logotype.setText(QCoreApplication.translate("Form", u"RB", None))
    # retranslateUi

