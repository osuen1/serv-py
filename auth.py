import psycopg2 as ps

def add_to_database(username, password):
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
