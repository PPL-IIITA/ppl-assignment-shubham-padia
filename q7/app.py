from helper import form_couple, get_girl_list, get_boy_list, get_gift_list, search
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
    couple_dict = {}
    committed_boys = []
    committed_girls = []

    for girl in girl_data:
        for boy in boy_data:
            if boy.single == 1:
                if form_couple(boy, girl):
                    couple = Couple(boy, girl, gift_list)
                    couple_list.append(couple)
                    couple_dict[boy.name] = girl.name
                    committed_boys.append(couple.boy.name)
                    committed_girls.append(couple.girl.name)
                    logging.info(boy.name + ' and ' + girl.name + ' are a couple.')
                    couple_writer.writerow([boy.name, girl.name, couple.happiness, couple.compatibility])
                    break

    search_boy = '31geek'
    for boy in committed_boys:
        print(boy)

    for couple in couple_list:
        if couple.boy.name == search_boy:
            print('Girlfriend of search query : ' + search_boy + ' by list implementation is ' + couple.girl.name)
            break

    pos = search(committed_boys, search_boy)
    if pos != -1:
        print('Girlfriend of search query : ' + search_boy + ' by Binary search implementation is ' + couple_dict.get(search_boy, 'no girlfriend'))
    else:
        print('The boy is single :( ')

    print('Girlfriend of search query : ' + search_boy + ' by hashtable implementation is ' + couple_dict.get(search_boy, 'no girlfriend'))


main()
