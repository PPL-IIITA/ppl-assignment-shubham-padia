import csv
import random
from boy import Boy
from girl import Girl
from gift import EssentialGift, LuxuryGift, UtilityGift
from Couple import Couple
import logging
logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S', level=logging.DEBUG)


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
        logging.info(boy.name + ' comitted with ' + girl.name)
        return True
    return False


def get_boy_list():
    """
    Autogenerates a random boy list
    :return:
    """
    boy_data = []
    for i in range(1, 30):
        boy_data.append(Boy(str(i)+'miser', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000), 'miser'))
        boy_data.append(Boy(str(i)+'generous', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000), 'generous'))
        boy_data.append(Boy(str(i)+'geek', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000), 'geek'))
    return boy_data


def get_girl_list():
    """
    autogenerates a random girl list
    :return:
    """
    girl_data = []
    for i in range(1, 10):
        girl_data.append(Girl(str(i)+'choosy', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000), 'choosy'))
        girl_data.append(Girl(str(i)+'normal', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000), 'normal'))
        girl_data.append(Girl(str(i)+'desperate', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000), 'desperate'))
    return girl_data


def get_gift_list(filename):
    """
    Extracts gift data from csv file
    :param filename: filename of the csv file
    :return: list of gift objects
    """
    gift_data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                if row[0] == 'essential':
                    gift_data.append(EssentialGift(row[1], row[2], row[3]))
                if row[1] == 'luxury':
                    gift_data.append(LuxuryGift(row[1], row[2], row[3], row[4], row[5]))
                if row[2] == 'utility':
                    gift_data.append(UtilityGift(row[1], row[2], row[3], row[4], row[5]))
    gift_data.sort(key=lambda x: x.price, reverse=True)
    return gift_data
