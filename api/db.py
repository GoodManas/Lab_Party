import sqlite3

db = sqlite3.connect('db/Work.db')
cursor = db.cursor()

if __name__ == "__main__":
    # Включаем поддержку внешних ключей (достаточно 1 раза)
    db.execute("PRAGMA foreign_keys = ON;")

    # Создаём таблицы
    db.execute('''
        CREATE TABLE IF NOT EXISTS role (
            id_role INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT         
        )
    ''')
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS type (
            id_type INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT            
        )
    ''')
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id_users INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            id_role INTEGER DEFAULT 2,
            is_admin BOOLEAN NOT NULL DEFAULT FALSE,
            FOREIGN KEY(id_role) REFERENCES role(id_role)
        )
    ''')
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS resources (
            id_resources INTEGER PRIMARY KEY AUTOINCREMENT,
            type INTEGER,
            description TEXT,
            FOREIGN KEY(type) REFERENCES type(id_type)
        )
    ''')    
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id_booking INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            resource_id INTEGER,
            start_time DATETIME,
            end_time DATETIME,
            status TEXT  DEFAULT 'pending',
            FOREIGN KEY(user_id) REFERENCES users(id_users),
            FOREIGN KEY(resource_id) REFERENCES resources(id_resources)
        )
    ''')

    # Заполняем таблицу type
    types = [('room',), ('equipment',)]
    cursor.executemany('INSERT OR IGNORE INTO type (type) VALUES (?)', types)
    
    # Заполняем таблицу role
    roles = [('Профессор',), ('Ученик',), ('Админ',)]
    cursor.executemany('INSERT OR IGNORE INTO role (role) VALUES (?)', roles)
    
    # Заполняем таблицу resources (type=1 - room, type=2 - equipment)
    resources = [
        ('1', 1, 'Лекционная аудитория на 50 мест'),
        ('10', 2, 'Переносной проектор Epson'),
        ('100', 1, 'Класс с 20 компьютерами')
    ]
    cursor.executemany('INSERT OR IGNORE INTO resources (id_resources, type, description) VALUES (?, ?, ?)', resources)
    
    db.commit()
    db.close()