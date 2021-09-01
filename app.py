from flask import Flask, render_template, url_for
from config import Config
from laboratory_database import LaboratoryDatabase
from app_users_database import AppUsersDatabase
from dict_terminology import COLS_INGGEO, ORDERS, COLS_CONSTRUCTION_SAND, COLS_QUARTZ_SAND
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)
laboratory_db = LaboratoryDatabase()
users_db = AppUsersDatabase()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


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
    ing_probes = []
    construction_sands = []
    quartz_sands = []
    for row in laboratory_db.get_all_order_ing_probes(int(order_id)):
        ing_probes.append(dict(zip(COLS_INGGEO.keys(), row)))
    for row in laboratory_db.get_all_order_construction_sand(int(order_id)):
        construction_sands.append(dict(zip(COLS_CONSTRUCTION_SAND.keys(), row)))
    for row in laboratory_db.get_all_order_quartz_sand(int(order_id)):
        quartz_sands.append(dict(zip(COLS_QUARTZ_SAND.keys(), row)))
    return render_template('all_order_probes.html', ing_probes=ing_probes, table_ing_header=COLS_INGGEO,
                           construction_sands=construction_sands, table_construction_header=COLS_CONSTRUCTION_SAND,
                           quartz_sands=quartz_sands, table_quartz_header=COLS_QUARTZ_SAND)


if __name__ == '__main__':
    app.run(debug=True)
