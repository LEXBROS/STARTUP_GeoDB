import psycopg2
from db_config import DB_USER, DB_PASSWORD, NAME_DB_1, HOST, PORT


def read_sql():
    with open('app_users_db_init.txt', 'r', encoding='utf-8') as sql_init:
        sqlcommand = sql_init.read()
    return sqlcommand


class AppUsersDatabase:

    def __init__(self, database=NAME_DB_1, user=DB_USER, password=DB_PASSWORD,
                 host=HOST, port=PORT):
        self._db = database
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        with psycopg2.connect(database=self._db,
                              user=self._user,
                              password=self._password,
                              host=self._host,
                              port=self._port) as connection:
            cur = connection.cursor()
            cur.execute(read_sql())
            connection.commit()
