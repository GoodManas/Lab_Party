import sqlite3

db = sqlite3.connect('db/Work.db')
cursor = db.cursor()

if __name__ == "__main__":
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id_users INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            id_role INT,
            is_admin BOOLEAN NOT NULL DEFAULT FALSE
            FOREIGN KEY(id_role) REFERENCES role(id_role)
);
''')
    db.execute('''
        CREATE TABLE IF NOT EXISTS resources (
            id_resources INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type INT ,
            description TEXT
            FOREIGN KEY(type) REFERENCES type(id_type)
);
''')    
    db.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id_booking INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            resource_id INTEGER NOT NULL,
            start_time DATETIME NOT NULL,
            end_time DATETIME NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(resource_id) REFERENCES resources(id)
)
''')
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS type (
            id_type INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            
)
''')
    
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS role (
            id_role INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            
)
''')
    
    
    
    resources = [
        ('Аудитория 101', 'room', 'Лекционная аудитория на 50 мест'),
        ('Проектор 1', 'equipment', 'Переносной проектор Epson'),
        ('Компьютерный класс 201', 'room', 'Класс с 20 компьютерами')
    ]

    cursor.executemany('INSERT OR IGNORE INTO resources (name, type, description) VALUES (?, ?, ?)', resources)
    db.commit()
    

    role = [
        ('Професор'),
        ('Ученик'),
        ('Админ')
    ]

    cursor.executemany('INSERT OR IGNORE INTO role (role) VALUES (?)', role)
    db.commit()