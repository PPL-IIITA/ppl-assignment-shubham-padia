from helper import form_couple, get_girl_list, get_boy_list
import csv

girl_data = get_girl_list('data/girl.csv')
boy_data = get_boy_list('data/boy.csv')
couple_file = open('./data/couples.csv', 'w+')
couple_writer = csv.writer(couple_file, delimiter=',')

for girl in girl_data:
    for boy in boy_data:
        if boy.single == 1:
            if form_couple(boy, girl):
                couple_writer.writerow([boy.name, girl.name])
                break