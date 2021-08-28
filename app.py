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
def new_obj():
    return render_template('new_obj.html')


@app.route('/change_obj')  # Выбор текущего объекта для работы
def change_obj():
    obj_list = laboratory_db.get_all_objects()
    return render_template('change_obj.html', obj_list=obj_list)


if __name__ == '__main__':
    app.run(debug=True)
