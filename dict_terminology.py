SOIL_TYPES = {
    '1': 'песчаный грунт',
    '2': 'глинистый грунт',
    '3': 'строительный песок',
    '4': 'кварцевый песок'
}

ORDERS = {
    'order_id': 'Номер заказа',
    'order_name': 'Название объекта',
    'client_id': 'Клиент id',
    'region': 'Регион',
    'order_city': 'Город',
    'order_address': 'Адрес',
    'order_year': 'Год начала выполнения'
}

COLS_INGGEO = {
    'probe_id': '№ пробы',
    'order_id': '№ заказа',
    'executor_id': 'Лаборант',
    'date_ready': 'Дата исп.',
    'skv': '№ скв.',
    'probe_num': '№ пробы',
    'probe_depth': 'Глуб. отбора',
    'soil_type': 'Тип грунта',
    'water_content': 'Прир. влажн.',
    'liquid_limit': 'Предел текуч.',
    'plastic_limit': 'Предел раск.',
    'plasticity_index': 'Число пласт.',
    'liquidity_index': 'Показат. консист.',
    'sito10': '>10',
    'sito5': '10-5',
    'sito2': '5-2',
    'sito1': '2-1',
    'sito0_5': '1-0.5',
    'sito0_25': '0.5-0.25',
    'sito0_1': '0.25-0.1',
    'sito0_05': '0.1-0.05',
    'sito0_01': '0.05-0.01',
    'sito0_002': '0.01-0.002',
    'sito_last': '<0.002',
    'density': 'Плотн. грунта',
    'particle_density': 'Плотн. част. гр.',
    'dry_density': 'Плотн. сух. гр.',
    'saturation_ratio': 'Ст. водонас.',
    'void_ratio': 'К-т пористости',
    'filtration': 'К-т фильтрации',
    'organic': 'Сод.орг.в-в',
    'uniformity_coefficient': 'К-т неоднородности гран.с-ва'
}

COLS_CONSTRUCTION_SAND = {
    'probe_id': '№ пробы',
    'order_id': '№ заказа',
    'executor_id': 'Лаборант',
    'date_ready': 'Дата исп.',
    'skv': '№ скв.',
    'probe_num': '№ пробы',
    'probe_up': 'Верх пробы',
    'probe_down': 'Низ пробы',
    'probe_length': 'Длина пробы',
    'soil_type': 'Тип пробы',
    'sito10': '>10',
    'sito5': '10-5',
    'sito2_5': '5-2.5',
    'sito1_25': '2.5-1.25',
    'sito0_63': '1.25-0.63',
    'sito0_315': '0.63-0.315',
    'sito0_16': '0.315-0.16',
    'sito_last': '<0.16',
    'dust': 'Пылевидн. и глинистые частицы',
    's_filtration': 'Коэффициент фильтрации при макс. плотности',
    'size_module': 'Модуль крупности',
    'bulk_density': 'Насыпная плотность',
    'otkos_s': 'Угол откоса сух.',
    'otkos_w': 'Угол откоса вдн.',

}

COLS_QUARTZ_SAND = {
    'probe_id': '№ пробы',
    'order_id': '№ заказа',
    'executor_id': 'Лаборант',
    'date_ready': 'Дата исп.',
    'skv': '№ скв.',
    'probe_num': '№ пробы',
    'probe_up': 'Верх пробы',
    'probe_down': 'Низ пробы',
    'probe_length': 'Длина пробы',
    'soil_type': 'Тип пробы',
    'sito2_5': '>2.5',
    'sito1_6': '2.5-1.6',
    'sito1': '1.6-1.0',
    'sito0_8': '1.0-0.8',
    'sito0_63': '0.8-0.63',
    'sito0_4': '0.63-0.4',
    'sito0_315': '0.4-0.315',
    'sito0_2': '0.315-0.2',
    'sito0_16': '0.2-0.16',
    'sito0_1': '0.16-0.1',
    'sito0_063': '0.1-0.063',
    'sito0_05': '0.063-0.05',
    'sito_last': '<0.05',
    'clay': 'Содерж. глинистых частиц',
    'w': 'Массовая доля влаги',
    'limit_strength': 'Предел прочности (для Ж)',
    'pH': 'pH',
    'sio2': 'SiO2',
    'tio2': 'TiO2',
    'al2o3': 'Al2O3',
    'fe2o3': 'Fe2O3',
    'mno': 'MnO',
    'na2o': 'Na2O',
    'k2o': 'K2O',
    'p2o5': 'P2O5',
    'so3sulf': 'SO3 сульфидн.',
    'ppp': 'ППП',
    'uniformity_coefficient': 'К-т однородности',
    'avg_size': 'Средний размер зерна',
    'gazopr': 'Газопроницаемость',
    'mark_f': 'Марка формовочного песка',
    'mark_g': 'Марка стекольного песка'
}
