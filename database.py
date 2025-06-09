import sqlite3
import hashlib


def create_tables():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    # Таблица пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            is_admin BOOLEAN NOT NULL DEFAULT FALSE
        )
    ''')

    # Таблица ресурсов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            description TEXT
        )
    ''')

    # Таблица бронирований
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            resource_id INTEGER NOT NULL,
            start_time DATETIME NOT NULL,
            end_time DATETIME NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(resource_id) REFERENCES resources(id)
        )
    ''')

    # Создаём тестовые данные
    # Тестовый администратор (логин: admin, пароль: admin)
    admin_password = hashlib.sha256('admin'.encode()).hexdigest()
    cursor.execute('INSERT OR IGNORE INTO users (username, password, is_admin) VALUES (?, ?, ?)',
                   ('admin', admin_password, True))

    # Тестовые ресурсы
    resources = [
        ('Аудитория 101', 'room', 'Лекционная аудитория на 50 мест'),
        ('Проектор 1', 'equipment', 'Переносной проектор Epson'),
        ('Компьютерный класс 201', 'room', 'Класс с 20 компьютерами')
    ]
    cursor.executemany('INSERT OR IGNORE INTO resources (name, type, description) VALUES (?, ?, ?)', resources)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_tables()