import psycopg2
from db_config import DB_USER, DB_PASSWORD, NAME_DB_2, HOST, PORT


def read_sql():
    with open('laboratory_db_init.txt', 'r', encoding='utf-8') as sql_init:
        sqlcommand = sql_init.read()
    return sqlcommand


class LaboratoryDatabase:

    def __init__(self, database=NAME_DB_2, user=DB_USER, password=DB_PASSWORD,
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

    def get_all_orders(self):
        with psycopg2.connect(database=self._db,
                              user=self._user,
                              password=self._password,
                              host=self._host,
                              port=self._port) as connection:
            cur = connection.cursor()
            cur.execute("SELECT * FROM orders ORDER BY order_year DESC")
            all_orders = cur.fetchall()
        return all_orders

    def get_all_order_ing_probes(self, order_id):
        with psycopg2.connect(database=self._db,
                              user=self._user,
                              password=self._password,
                              host=self._host,
                              port=self._port) as connection:
            cur = connection.cursor()
            cur.execute("SELECT * FROM ing_probes WHERE order_id = %s", (order_id, ))
            all_probes_current_order = cur.fetchall()
        return all_probes_current_order

    def get_all_order_quartz_sand(self, order_id):
        with psycopg2.connect(database=self._db,
                              user=self._user,
                              password=self._password,
                              host=self._host,
                              port=self._port) as connection:
            cur = connection.cursor()
            cur.execute("SELECT * FROM quartz_sand WHERE order_id = %s", (order_id, ))
            all_quartz_sand_current_order = cur.fetchall()
        return all_quartz_sand_current_order

    def get_all_order_construction_sand(self, order_id):
        with psycopg2.connect(database=self._db,
                              user=self._user,
                              password=self._password,
                              host=self._host,
                              port=self._port) as connection:
            cur = connection.cursor()
            cur.execute("SELECT * FROM construction_sand WHERE order_id = %s", (order_id, ))
            all_construction_sand_current_order = cur.fetchall()
        return all_construction_sand_current_order
