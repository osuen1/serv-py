import psycopg2 as ps
import os
from dotenv import load_dotenv

load_dotenv()
usr = os.getenv('USER')
password = os.getenv('PASSWORD')

def add_to_dialog_session(request):
    with ps.connect(dbname='app', user=usr, password=password, host='localhost', port='5432') as conn:
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
