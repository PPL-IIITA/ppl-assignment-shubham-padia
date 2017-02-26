import csv
from boy import Boy
from girl import Girl
import random


def form_couple(boy, girl):
    """
    Takes a boy and girl and forms it couple
    :param boy: boy object
    :param girl: girl object
    :return:
    """
    if girl.budget <= boy.budget and boy.min_attraction <= girl.attractiveness:
        girl.change_commitment()
        boy.change_commitment()
        return True
    return False


def get_boy_list():
    """
    Autogenerates a random boy list
    :return:
    """
    boy_data = []
    for i in range(1, 90):
        boy_data.append(Boy(str(i), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000)))
    return boy_data


def get_girl_list():
    """
    autogenerates a random girl list
    :return:
    """
    girl_data = []
    for i in range(1, 30):
        girl_data.append(Girl(str(i), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000)))
    return girl_data


