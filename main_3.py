import os
import csv
import datetime

from decimal import Decimal


# file_path = 'E:\\R\\python_projects\\b_data\\data\\data_LTC'
file_path = 'F:\\data\\data_BTC'
file_list = os.listdir(file_path)
print(file_list)

percent_counter = Decimal('0.0000')
counter_long = Decimal('0.0000')
counter_short = Decimal('0.0000')
pointer = 0.0
flag_start = True
# open_time_list = []
open_list = []
# high_list = []
# low_list = []
# close_list = []
# volume_list = []
# close_time_list = []
    
    
for file in file_list:
    print(file)
    with open(os.path.join(file_path, file), newline='\n') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            # open_time_list.append(int(row[0]))
            open_list.append(Decimal(row[1]))
            # high_list.append(float(row[2]))
            # low_list.append(float(row[3]))
            # close_list.append(float(row[4]))
            # volume_list.append(float(row[5]))
            # close_time_list.append(int(row[6]))
    
    if flag_start:
        pointer = open_list[0]
        flag_start = False
    
    for i in range(len(open_list)):
        if (pointer / open_list[i]) < 0.9985 or (pointer / open_list[i]) > 1.0015:
            if pointer / open_list[i] < 0.9985:
                counter_long += Decimal('0.0005')
            
            if pointer / open_list[i] > 1.0015:
                counter_short += Decimal('0.0005')
            
            pointer = open_list[i]
            percent_counter += Decimal('0.0005')
            
            
    
    open_list.clear()


print(f'Percent counter: {percent_counter}')
print(f'Counter LONG: {counter_long}')
print(f'Counter SHORT: {counter_short}')
    