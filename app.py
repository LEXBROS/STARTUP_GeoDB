from flask_bootstrap import Bootstrap
from flask import Flask, render_template, url_for, request, session, redirect
from config import Config
from laboratory_database import LaboratoryDatabase
from app_users_database import AppUsersDatabase
from dict_terminology import COLS_INGGEO, ORDERS, COLS_CONSTRUCTION_SAND, COLS_QUARTZ_SAND
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user
from userlogin import UserLogin

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
laboratory_db = LaboratoryDatabase()
users_db = AppUsersDatabase()


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().from_db(user_id, users_db)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hash = generate_password_hash(form.password.data)
        res = users_db.adduser(form.email.data, hash, form.first_name.data, form.last_name.data)
        if res:
            print('Успешная регистрация')
            return redirect(url_for('login'))
        else:
            print('Че-то не то с регистрацией')
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users_db.getUserByEmail(form.email.data)
        print(user)
        if user and check_password_hash(user['password'], form.password.data):
            userlogin = UserLogin().create(user)
            rm = form.remember.data
            login_user(userlogin, remember=rm)
            return redirect(request.args.get("next") or url_for("index"))

    return render_template("login.html", form=form)


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
