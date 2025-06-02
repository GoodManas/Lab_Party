# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Auth(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 470)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-120, -50, 931, 531))
        self.widget.setStyleSheet(u"background-color: rgb(255, 160, 182)")
        self.btn_Login = QPushButton(self.widget)
        self.btn_Login.setObjectName(u"btn_Login")
        self.btn_Login.setGeometry(QRect(170, 300, 141, 41))
        self.btn_Login.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton#loginButton {\n"
"    background-color: var(--primary);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    opacity: 0.9;\n"
"}")
        self.btn_register = QPushButton(self.widget)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(330, 290, 131, 61))
        self.btn_register.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton#loginButton {\n"
"    background-color: var(--primary);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    opacity: 0.9;\n"
"}")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(250, 190, 113, 22))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 160, 49, 16))
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(250, 260, 113, 22))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 230, 49, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_Login.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.btn_register.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u043b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

