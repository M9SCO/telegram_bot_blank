import psycopg2
import json
file = open("bin/constants")
const = json.loads(file.read())
cnx = psycopg2.connect(host=const["bd"]["host"],dbname=const["bd"]["name"], user=const["bd"]["user"], password=const["bd"]["pass"])
file.close()
cnx.set_session(autocommit=True)
cursor = cnx.cursor()

def db_command(SQL_request):
    if 'select' in SQL_request.lower():
        cursor.execute(SQL_request)
        row = cursor.fetchall()
        return row
    else:
        cursor.execute(SQL_request)