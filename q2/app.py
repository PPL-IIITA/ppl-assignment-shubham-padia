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

    for girl in girl_data:
        for boy in boy_data:
            if boy.single == 1:
                if form_couple(boy, girl):
                    gift_list = get_gift_list('data/gifts.csv')
                    couple = Couple(boy, girl, gift_list)
                    couple_list.append(couple)
                    logging.info(boy.name + ' and ' + girl.name + ' are a couple.')
                    couple_writer.writerow([boy.name, girl.name, couple.happiness, couple.compatibility])
                    break
    k = int(input("To find out the k most happiest couple enter k: \n"))
    couple_list.sort(key=lambda x: x.happiness, reverse=True)
    for i in range(0, k):
        print(couple_list[i])


main()