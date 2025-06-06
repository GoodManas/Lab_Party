import sys
import sqlite3
import hashlib
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QTableWidgetItem, 
    QHeaderView, QMessageBox, QTabWidget, QPushButton, QLineEdit,
    QLabel, QVBoxLayout, QHBoxLayout, QDateTimeEdit, QComboBox, QTableWidget
)
from database import create_tables
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QFont


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Авторизация')
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        self.username = QLineEdit()
        self.username.setPlaceholderText('Логин')
        self.password = QLineEdit()
        self.password.setPlaceholderText('Пароль')
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_btn = QPushButton('Войти')
        self.login_btn.clicked.connect(self.authenticate)
        self.register_btn = QPushButton('Регистрация')
        self.register_btn.clicked.connect(self.open_register)

        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.register_btn)

        self.setLayout(layout)

    def authenticate(self):
        username = self.username.text()
        password = hashlib.sha256(self.password.text().encode()).hexdigest()

        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, is_admin FROM users WHERE username=? AND password=?',
            (username, password)
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            self.user_id = user[0]
            self.is_admin = user[1]
            self.accept()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль')

    def open_register(self):
        self.register_window = RegisterWindow()
        self.register_window.exec()


class RegisterWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Регистрация')
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        self.username = QLineEdit()
        self.username.setPlaceholderText('Логин')
        self.password = QLineEdit()
        self.password.setPlaceholderText('Пароль')
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.register_btn = QPushButton('Зарегистрироваться')
        self.register_btn.clicked.connect(self.register)

        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.register_btn)

        self.setLayout(layout)

    def register(self):
        username = self.username.text()
        password = hashlib.sha256(self.password.text().encode()).hexdigest()

        if not username or not self.password.text():
            QMessageBox.warning(self, 'Ошибка', 'Заполните все поля')
            return

        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)',
                (username, password)
            )
            conn.commit()
            QMessageBox.information(self, 'Успех', 'Регистрация успешна')
            self.accept()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Ошибка', 'Логин уже занят')
        finally:
            conn.close()


class MainWindow(QMainWindow):
    def __init__(self, user_id, is_admin):
        super().__init__()
        self.user_id = user_id
        self.is_admin = is_admin
        self.initUI()
        self.load_data()

    def initUI(self):
        self.setWindowTitle('Система бронирования ресурсов')
        self.setMinimumSize(800, 600)

        self.tabs = QTabWidget()

        # Вкладка расписания
        self.schedule_tab = QWidget()
        self.schedule_table = self.create_table(['Ресурс', 'Тип', 'Начало', 'Конец', 'Статус'])
        self.refresh_btn = QPushButton('Обновить')
        self.refresh_btn.clicked.connect(self.load_data)
        self.new_booking_btn = QPushButton('Новое бронирование')
        self.new_booking_btn.clicked.connect(self.open_booking_dialog)

        tab_layout = QVBoxLayout()
        tab_layout.addWidget(self.schedule_table)
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.refresh_btn)
        btn_layout.addWidget(self.new_booking_btn)
        tab_layout.addLayout(btn_layout)
        self.schedule_tab.setLayout(tab_layout)

        self.tabs.addTab(self.schedule_tab, 'Расписание')

        # Вкладка для администратора
        if self.is_admin:
            self.admin_tab = QWidget()
            self.admin_table = self.create_table(['Ресурс', 'Пользователь', 'Начало', 'Конец', 'Статус'])
            self.approve_btn = QPushButton('Подтвердить')
            self.reject_btn = QPushButton('Отклонить')
            self.approve_btn.clicked.connect(lambda: self.update_booking_status('approved'))
            self.reject_btn.clicked.connect(lambda: self.update_booking_status('rejected'))

            admin_layout = QVBoxLayout()
            admin_layout.addWidget(self.admin_table)
            btn_layout_admin = QHBoxLayout()
            btn_layout_admin.addWidget(self.approve_btn)
            btn_layout_admin.addWidget(self.reject_btn)
            admin_layout.addLayout(btn_layout_admin)
            self.admin_tab.setLayout(admin_layout)
            self.tabs.addTab(self.admin_tab, 'Управление бронированиями')

        self.setCentralWidget(self.tabs)

    def create_table(self, headers):
        table = QTableWidget()
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        return table

    def load_data(self):
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        # Загрузка расписания
        cursor.execute('''
            SELECT r.name, r.type, b.start_time, b.end_time, b.status 
            FROM bookings b
            JOIN resources r ON b.resource_id = r.id
            ORDER BY b.start_time
        ''')
        data = cursor.fetchall()

        self.schedule_table.setRowCount(len(data))
        for row_idx, row in enumerate(data):
            for col_idx, item in enumerate(row):
                self.schedule_table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

        # Загрузка данных для администратора
        if self.is_admin:
            cursor.execute('''
                SELECT r.name, u.username, b.start_time, b.end_time, b.status 
                FROM bookings b
                JOIN resources r ON b.resource_id = r.id
                JOIN users u ON b.user_id = u.id
                ORDER BY b.start_time
            ''')
            admin_data = cursor.fetchall()

            self.admin_table.setRowCount(len(admin_data))
            for row_idx, row in enumerate(admin_data):
                for col_idx, item in enumerate(row):
                    self.admin_table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

        conn.close()

    def open_booking_dialog(self):
        self.booking_dialog = BookingDialog(self.user_id)
        if self.booking_dialog.exec():
            self.load_data()

    def update_booking_status(self, status):
        if not self.is_admin:
            return

        selected = self.admin_table.currentRow()
        if selected == -1:
            return

        booking_id = self.admin_table.item(selected, 0).text()
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE bookings SET status = ? WHERE id = ?',
            (status, booking_id)
        )
        conn.commit()
        conn.close()
        self.load_data()


class BookingDialog(QDialog):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle('Новое бронирование')
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        self.resource_cb = QComboBox()
        self.load_resources()

        self.start_time = QDateTimeEdit()
        self.start_time.setDateTime(QDateTime.currentDateTime())
        self.end_time = QDateTimeEdit()
        self.end_time.setDateTime(QDateTime.currentDateTime().addSecs(3600))

        self.submit_btn = QPushButton('Создать')
        self.submit_btn.clicked.connect(self.submit_booking)

        layout.addWidget(QLabel('Ресурс:'))
        layout.addWidget(self.resource_cb)
        layout.addWidget(QLabel('Начало:'))
        layout.addWidget(self.start_time)
        layout.addWidget(QLabel('Конец:'))
        layout.addWidget(self.end_time)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)

    def load_resources(self):
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, type FROM resources')
        self.resources = cursor.fetchall()
        conn.close()

        self.resource_cb.clear()
        for resource in self.resources:
            self.resource_cb.addItem(f"{resource[1]} ({resource[2]})", resource[0])

    def submit_booking(self):
        resource_id = self.resource_cb.currentData()
        start = self.start_time.dateTime().toString(Qt.DateFormat.ISODate)
        end = self.end_time.dateTime().toString(Qt.DateFormat.ISODate)

        # Проверка на конфликты
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT COUNT(*) FROM bookings 
            WHERE resource_id = ? AND (
                (start_time BETWEEN ? AND ?) OR
                (end_time BETWEEN ? AND ?) OR
                (start_time <= ? AND end_time >= ?)
            )
        ''', (resource_id, start, end, start, end, start, end))
        conflict = cursor.fetchone()[0]

        if conflict > 0:
            QMessageBox.warning(self, 'Ошибка', 'Конфликт времени бронирования')
            conn.close()
            return

        cursor.execute('''
            INSERT INTO bookings (user_id, resource_id, start_time, end_time)
            VALUES (?, ?, ?, ?)
        ''', (self.user_id, resource_id, start, end))
        conn.commit()
        conn.close()
        self.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создаем окно входа
    login = LoginWindow()
    if login.exec():
        user_id = login.user_id
        is_admin = login.is_admin
        main_window = MainWindow(user_id, is_admin)
        main_window.show()
        sys.exit(app.exec())