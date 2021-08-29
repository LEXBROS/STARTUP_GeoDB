from flask import Flask, render_template, url_for
from laboratory_database import LaboratoryDatabase
from app_users_database import AppUsersDatabase
from dict_terminology import DT

app = Flask(__name__)
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
    orders = [{
        'order_id': order_id,
        'order_name': order_name,
        'client_id': client_id,
        'region': region,
        'order_city': order_city,
        'order_address': order_address,
        'order_year': order_year
    } for order_id, order_name, client_id, region, order_city, order_address, order_year in
        laboratory_db.get_all_orders()]
    return render_template('change_order.html', orders_list=orders)


@app.route('/current_order/<int:order_id>')
def current_order(order_id):
    probes = [{
        'probe_id': probe_id,
        'order_id': order_id_,
        'executor_id': executor_id,
        'date_ready': date_ready,
        'skv': skv,
        'probe_depth': probe_depth,
        'soil_type': soil_type,
        'water_content': water_content,
        'liquid_limit': liquid_limit,
        'plastic_limit': plastic_limit,
        'plasticity_index': plasticity_index,
        'liquidity_index': liquidity_index,
        'sito10': sito10,
        'sito5': sito5,
        'sito2': sito2,
        'sito1': sito1,
        'sito0_5': sito0_5,
        'sito0_25': sito0_25,
        'sito0_1': sito0_1,
        'sito0_05': sito0_05,
        'sito0_01': sito0_01,
        'sito0_002': sito0_002,
        'sito_last': sito_last,
        'density': density,
        'particle_density': particle_density,
        'dry_density': dry_density,
        'saturation_ratio': saturation_ratio,
        'void_ratio': void_ratio,
        'filtration': filtration,
        'organic': organic,
        'uniformity_coefficient': uniformity_coefficient
    } for
        probe_id, order_id_, executor_id, date_ready, skv, probe_depth, soil_type, water_content, liquid_limit,
        plastic_limit, plasticity_index, liquidity_index, sito10, sito5, sito2, sito1, sito0_5, sito0_25, sito0_1,
        sito0_05, sito0_01, sito0_002, sito_last, density, particle_density, dry_density, saturation_ratio,
        void_ratio, filtration, organic, uniformity_coefficient in laboratory_db.get_current_order(int(order_id))]
    return render_template('current_order.html', probes=probes, table_header=DT)


if __name__ == '__main__':
    app.run(debug=True)
