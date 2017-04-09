import csv
import random
from boy import MiserBoy, GeekBoy, GenerousBoy
from girl import ChoosyGirl, NormalGirl, DesperateGirl
from gift import EssentialGift, LuxuryGift, UtilityGift
from Couple import Couple
import logging
from bisect import bisect_left

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
    boy_data = [GeekBoy('31geek', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000))]
    for i in range(1, 30):
        boy_data.append(MiserBoy(str(i)+'miser', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000)))
        boy_data.append(GenerousBoy(str(i)+'generous', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000)))
        boy_data.append(GeekBoy(str(i)+'geek', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000)))
    return boy_data


def get_girl_list():
    """
    autogenerates a random girl list
    :return:
    """
    girl_data = []
    for i in range(1, 10):
        girl_data.append(ChoosyGirl(str(i)+'choosy', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000)))
        girl_data.append(NormalGirl(str(i)+'normal', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000)))
        girl_data.append(DesperateGirl(str(i)+'desperate', random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 10000)))
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


def search(lst, target):
    min = 0
    max = len(lst)-1
    avg = (min+max)/2
    # uncomment next line for traces
    # print lst, target, avg
    while min < max:
        if lst[avg] == target:
            return avg
        elif lst[avg] < target:
            return avg + 1 + search(lst[avg+1:], target)
        else:
            return search(lst[:avg], target)

    # avg may be a partial offset so no need to print it here
    # print "The location of the number in the array is", avg
    return avg
