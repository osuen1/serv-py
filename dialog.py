import psycopg2 as ps

def add_to_dialog_session(request):
    with ps.connect(dbname='app', user='postgres', password='12345678', host='localhost', port='5432') as conn:
        if conn:
            try:
                curs = conn.cursor()

                curs.execute(
                    f'''
                        INSERT INTO dialog(users_message)
                        VALUES ('{request}');
                    '''
                )

                conn.commit()
            except Exception as e:
                conn.rollback()
                print(e)
