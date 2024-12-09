import psycopg2 as ps

def add_to_database(username, password): # добавляем пользователя
    with ps.connect(dbname='app', user='postgres', password='12345678', host='localhost', port='5432') as conn:
        if conn:
            curs = conn.cursor()

            curs.execute(
                f'''
                    INSERT INTO users(login, password)
                    VALUES ('{username}', '{password}');
                '''
            )

            conn.commit()
            curs.close()

def check_user(username, password): # проверяем наличие пользователя
    with ps.connect(dbname='app', user='postgres', password='12345678', host='localhost', port='5432') as conn:
        if conn:
            curs = conn.cursor()
            
            curs.execute(
                f'''
                    SELECT * FROM users WHERE login = %s AND password = %s;
                ''', (username, password)
            )
            result = curs.fetchone()

            if result is None:
                return False
            else:
                return True