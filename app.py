from flask import Flask, render_template, url_for
from laboratory_database import LaboratoryDatabase
from app_users_database import AppUsersDatabase

app = Flask(__name__)
laboratory_db = LaboratoryDatabase()
users_db = AppUsersDatabase()


@app.route('/')
@app.route('/index')  # Главная страница
def index():
    return render_template('index.html')


@app.route('/new_obj')  # Добавление нового объекта
def new_order():
    return render_template('new_obj.html')


@app.route('/change_obj')  # Выбор текущего объекта для работы
def change_order():
    orders = [{
        'order_id': order_id,
        'order_name': order_name,
        'client_id': client_id,
        'region': region,
        'order_city': order_city,
        'order_address': order_address,
        'order_year': order_year
    } for order_id, order_name, client_id, region, order_city, order_address, order_year in
        laboratory_db.get_all_objects()]
    return render_template('change_order.html', orders_list=orders)


if __name__ == '__main__':
    app.run(debug=True)
