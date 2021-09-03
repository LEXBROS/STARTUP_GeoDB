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

    def adduser(self, email, hashpsw, first_name, last_name):
        try:
            with psycopg2.connect(database=self._db,
                                  user=self._user,
                                  password=self._password,
                                  host=self._host,
                                  port=self._port) as connection:
                cur = connection.cursor()
                cur.execute("""INSERT INTO app_users.public.users (email, password, first_name, last_name)
                            VALUES (%s, %s, %s, %s)""", (email, hashpsw, first_name, last_name))
            return True
        except psycopg2.OperationalError:
            return False

    def getuser(self, user_id):
        try:
            with psycopg2.connect(database=self._db,
                                  user=self._user,
                                  password=self._password,
                                  host=self._host,
                                  port=self._port) as connection:
                cur = connection.cursor()
                cur.execute("""SELECT * FROM app_users.public.users WHERE id = %s""", (user_id,))
                res = cur.fetchone()
                if not res:
                    print('Пльзователь не найден')
                    return False
        except psycopg2.OperationalError as e:
            print("Ошибка получения данных из БД " + str(e))
        return False

    def getUserByEmail(self, user_email):
        try:
            with psycopg2.connect(database=self._db,
                                  user=self._user,
                                  password=self._password,
                                  host=self._host,
                                  port=self._port) as connection:
                cur = connection.cursor()
                cur.execute("""SELECT * FROM app_users.public.users WHERE email = %s""", (user_email,))
                res = cur.fetchone()
                user_ = dict(zip(['id', 'email', 'password', 'first_name', 'last_name'], res))
                return user_
        except psycopg2.OperationalError as e:
            print("Ошибка получения данных из БД " + str(e))
        return False
