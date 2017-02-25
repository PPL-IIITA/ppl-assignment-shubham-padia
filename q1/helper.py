import csv
from boy import Boy
from girl import Girl


def form_couple(boy, girl):
    if girl.budget <= boy.budget and boy.min_attraction <= girl.attractiveness:
        girl.change_commitment()
        boy.change_commitment()
        return True
    return False


def get_boy_list(filename):
    boy_data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                boy_data.append(Boy(row[0], row[1], row[2], row[3], row[4], 1))
    return boy_data


def get_girl_list(filename):
    girl_data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                girl_data.append(Girl(row[0], row[1], row[2], row[3], row[4]))
    return girl_data
