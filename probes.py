import datetime
from ing_csv_to_db import normalize_ing_csv


class IngProbes:
    headers = ('order_id', 'executor_id', 'date_ready',
               'skv', 'probe_num', 'probe_depth', 'soil_type', 'water_content',
               'liquid_limit', 'plastic_limit', 'plasticity_index',
               'liquidity_index', 'sito10', 'sito5', 'sito2', 'sito1',
               'sito0_5', 'sito0_25', 'sito0_1', 'sito0_05', 'sito0_01',
               'sito0_002', 'sito_last', 'density', 'particle_density',
               'dry_density', 'saturation_ratio', 'void_ratio',
               'filtration', 'organic',
               'uniformity_coefficient')

    def __init__(self, order_id, executor_id, *args):
        self.order_id = int(order_id)
        self.executor_id = int(executor_id)
        self.date_ready = datetime.date
        self.skv = str(args[0])
        self.probe_num = str(args[1])
        self.probe_depth = float(args[2])
        self.soil_type = int(args[3])
        self.water_content = float(args[4])
        self.liquid_limit = float(args[5])
        self.plastic_limit = float(args[6])
        self.plasticity_index = round(float(self.liquid_limit) - float(self.plastic_limit), 2)
        self.liquidity_index = (float(self.water_content) - float(self.plastic_limit)) / self.plasticity_index
        self.sito10 = float(args[7])
        self.sito5 = float(args[8])
        self.sito2 = float(args[9])
        self.sito1 = float(args[10])
        self.sito0_5 = float(args[11])
        self.sito0_25 = float(args[12])
        self.sito0_1 = float(args[13])
        self.sito0_05 = float(args[14])
        self.sito0_01 = float(args[15])
        self.sito0_002 = float(args[16])
        self.sito_last = float(args[17])
        self.density = float(args[18])
        self.particle_density = float(args[19])
        # TODO
        # self.dry_density =
        # self.saturation_ratio =
        # self.void_ratio =
        # self.filtration =
        # self.organic =
        # self.uniformity_coefficient =






    def get_full_tuple(self):
        pass


class ConstructionSandProbes:

    def __init__(self):
        pass

    def get_full_tuple(self):
        pass


class QuartzSandProbes:

    def __init__(self):
        pass

    def get_full_tuple(self):
        pass


# tests
a = IngProbes(1, 1, normalize_ing_csv('ing_probes_.csv'))
