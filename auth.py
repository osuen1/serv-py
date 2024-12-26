import psycopg2 as ps
from dotenv import load_dotenv
import os

load_dotenv()
usr = os.getenv('USER')
password = os.getenv('PASSWORD')

def connect(data):
    with ps.connect(dbname='app', user=usr, password=password, host='localhost', port='5432') as conn:
        if conn:
            curs = conn.cursor()

            curs.execute(data)

            conn.commit()
            result = curs.fetchone()
            
            curs.close()
            return result

def add_to_database(username, password): # добавляем пользователя
    return f'''
            INSERT INTO users(login, password)
            VALUES ('{username}', '{password}');
        '''

def check_user(username, password): # проверяем наличие пользователя
    result = connect(f''' SELECT * FROM users WHERE login = '{username}' AND password = '{password}'; ''')

    if result is None:
        return False
    else:
        return True