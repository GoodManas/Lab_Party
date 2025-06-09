from .db import db
import datetime
import sqlite3

#функция входа===========================
def login(login: str, passw: str):

	value = db.execute(f'''
		SELECT id_users, login, password, id_role FROM users 
		WHERE login='{login}' AND password='{passw}'; 
	''').fetchone()

	

	if value:
		return {
        	'id_users': value[0],
            'login': value[1],
            'id_role': value[3],
        }
	raise Exception(f'Unauthorized: User with login "{login}" not found or wrong password')

#===============================================================================
def register(login, passw):
	value = db.execute(f'''
		SELECT * FROM users 
		WHERE login='{login}'; 
	''').fetchall()
	if value:
		raise Exception("User with this login already exists")

	db.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{passw}')")
	db.commit()
 
def get_all_users():  
    value = db.execute('SELECT * FROM bookings;').fetchall()
    return value

def add_bron(id):
	db.execute(f"INSERT INTO bookings(resource_id) VALUES ('{id}')")
	db.commit()

def uchet(name,room):
	db.execute(f"INSERT INTO bookings(user_id, resource_id) VALUES ('{name}', '{room}')")
	
	db.commit()
	
	

#===============================================================================




