from PySide6.QtCore import QCoreApplication, QRect, QMetaObject
from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                               QCheckBox, QHBoxLayout, QListWidget, QSizePolicy)

class UiReservationSystem(object):
    def setupUi(self, Form):
        # Проверка и установка имени формы
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(400, 600)

        # Общий стиль формы
        Form.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, "
            "stop:0.00568182 rgba(255, 151, 191, 255), stop:1 rgba(255, 106, 138, 255))"
        )

        # Заголовок
        self.label_title = QLabel(Form)
        self.label_title.setObjectName("label_title")
        self.label_title.setGeometry(QRect(30, 20, 340, 30))
        font_title = self._create_font(16)
        self.label_title.setFont(font_title)
        self.label_title.setStyleSheet("background-color: rgba(85, 255, 255, 0); color: rgb(255, 230, 255);")

        # Ввод преподавателя
        self.label_professor = QLabel(Form)
        self.label_professor.setObjectName("label_professor")
        self.label_professor.setGeometry(QRect(30, 60, 150, 20))
        self.lineEdit_professor = QLineEdit(Form)
        self.lineEdit_professor.setObjectName("lineEdit_professor")
        self.lineEdit_professor.setGeometry(QRect(30, 85, 330, 22))
        self.lineEdit_professor.setPlaceholderText("Введите имя преподавателя")

        # Ввод кабинета
        self.label_room = QLabel(Form)
        self.label_room.setObjectName("label_room")
        self.label_room.setGeometry(QRect(30, 115, 150, 20))
        self.lineEdit_room = QLineEdit(Form)
        self.lineEdit_room.setObjectName("lineEdit_room")
        self.lineEdit_room.setGeometry(QRect(30, 140, 330, 22))
        self.lineEdit_room.setPlaceholderText("Введите название кабинета")

        # Ресурсы
        self.label_resources = QLabel(Form)
        self.label_resources.setObjectName("label_resources")
        self.label_resources.setGeometry(QRect(30, 170, 150, 20))
        self.resources_layout = QHBoxLayout()

        self.checkbox_board = QCheckBox("Доска", Form)
        self.checkbox_board.setObjectName("checkbox_board")
        self.checkbox_microphone = QCheckBox("Микрофон", Form)
        self.checkbox_microphone.setObjectName("checkbox_microphone")

        self.resources_widget = QWidget(Form)
        self.resources_widget.setObjectName("resources_widget")
        self.resources_widget.setGeometry(QRect(30, 200, 330, 40))
        self.resources_widget.setLayout(self.resources_layout)

        self.resources_layout.addWidget(self.checkbox_board)
        self.resources_layout.addWidget(self.checkbox_microphone)

        # Кнопка бронирования
        self.button_reserve = QPushButton(Form)
        self.button_reserve.setObjectName("button_reserve")
        self.button_reserve.setGeometry(QRect(30, 250, 330, 40))
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button_reserve.setSizePolicy(size_policy)
        self.button_reserve.setStyleSheet(
            "background-color: rgb(255, 200, 255); border: 1px solid rgb(255, 255, 255);"
            "border-radius: 10px; color: rgb(125, 41, 62);"
        )

        # Заголовок для текущих бронирований
        self.label_current = QLabel(Form)
        self.label_current.setObjectName("label_current")
        self.label_current.setGeometry(QRect(30, 310, 340, 20))
        font_subtitle = self._create_font(12)
        self.label_current.setFont(font_subtitle)
        self.label_current.setText("Текущие бронирования (для студентов):")
        self.label_current.setStyleSheet("color: rgb(255, 255, 255);")

        # Список бронирований
        self.list_widget = QListWidget(Form)
        self.list_widget.setObjectName("list_widget")
        self.list_widget.setGeometry(QRect(30, 340, 340, 230))

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Система бронирования кабинета"))
        self.label_title.setText(_translate("Form", "Бронирование кабинета для преподавателя"))
        self.label_professor.setText(_translate("Form", "Преподаватель:"))
        self.label_room.setText(_translate("Form", "Кабинет:"))
        self.label_resources.setText(_translate("Form", "Ресурсы:"))
        self.button_reserve.setText(_translate("Form", "Зарезервировать"))

    def _create_font(self, size):
        from PySide6.QtGui import QFont
        font = QFont()
        font.setPointSize(size)
        return font


