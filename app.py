from flask import Flask, render_template, url_for
from config import Config
from laboratory_database import LaboratoryDatabase
from app_users_database import AppUsersDatabase
from dict_terminology import COLS_INGGEO, ORDERS

app = Flask(__name__)
app.config.from_object(Config)
laboratory_db = LaboratoryDatabase()
users_db = AppUsersDatabase()


@app.route('/')
@app.route('/index')  # Главная страница
def index():
    return render_template('index.html')


@app.route('/new_order')  # Добавление нового объекта
def new_order():
    return render_template('new_order.html')


@app.route('/change_obj')  # Выбор текущего объекта для работы
def change_order():
    orders = []
    for row in laboratory_db.get_all_orders():
        orders.append(dict(zip(ORDERS.keys(), row)))
    return render_template('change_order.html', orders_list=orders)


@app.route('/all_order_probes/<int:order_id>')
def all_order_probes(order_id):
    probes = []
    for row in laboratory_db.get_all_order_probes(int(order_id)):
        probes.append(dict(zip(COLS_INGGEO.keys(), row)))
    return render_template('all_order_probes.html', probes=probes, table_header=COLS_INGGEO)


if __name__ == '__main__':
    app.run(debug=True)
