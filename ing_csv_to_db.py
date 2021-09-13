import csv


def normalize_ing_csv(filename):
    file = filename  # debug
    with open(file) as f:
        reader = csv.reader(f)  # iterator по файлу
        for row in reader:
            print(tuple(row[0].split(';')))


normalize_ing_csv('ing_probes_.csv')
