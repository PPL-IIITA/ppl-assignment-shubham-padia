from helper import form_couple, get_girl_list, get_boy_list, get_gift_list
from Couple import Couple
import csv
import logging
logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S', level=logging.DEBUG)


def main():
    girl_data = get_girl_list()
    boy_data = get_boy_list()
    couple_file = open('./data/couples.csv', 'w+')
    couple_writer = csv.writer(couple_file, delimiter=',')
    couple_list = []
    gift_list = get_gift_list('data/gifts.csv')

    for girl in girl_data:
        for boy in boy_data:
            if boy.single == 1:
                if form_couple(boy, girl):
                    couple = Couple(boy, girl, gift_list)
                    couple_list.append(couple)
                    logging.info(boy.name + ' and ' + girl.name + ' are a couple.')
                    couple_writer.writerow([boy.name, girl.name, couple.happiness, couple.compatibility])
                    break

    for couple in couple_list:
        print(couple.happiness)
    t = int(input("Enter t: \n"))

    couple_list.sort(key=lambda x: x.happiness)
    for couple in couple_list:
        if couple.happiness < t:
            couple.breakup()
            girl = couple.girl
            for boy in boy_data:
                if boy.single == 1 and boy != couple.boy:
                    form_couple(boy, girl)
                    couple = Couple(boy, girl, gift_list)
                    logging.info(boy.name + ' and ' + girl.name + ' are a new couple after breakup.')
                    print(boy.name + ' and ' + girl.name + ' are a new couple after breakup.')
                    couple_writer.writerow([boy.name, girl.name, couple.happiness, couple.compatibility])
                    break

main()
