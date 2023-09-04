import os
import csv
import datetime

from decimal import Decimal


file_path = 'F:\\data\\data_BTC'
file_list = os.listdir(file_path)
print(file_list)

# percent_counter = Decimal('0.0000')
# counter_long = Decimal('0.0000')
# counter_short = Decimal('0.0000')
balance = Decimal('10000.00')
pointer = 0.0
flag_start = True
open_list = []
dict_tmp = {}
price_tmp = Decimal('0.0')
    

for file in file_list:
    print(file)
    with open(os.path.join(file_path, file), newline='\n') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            open_list.append(Decimal(row[1]))
    
    if flag_start:
        pointer = open_list[0]
        flag_start = False
    
    
    for i in range(len(open_list)):
        if (pointer / open_list[i]) < Decimal('0.999') or (pointer / open_list[i]) > Decimal('1.001'):
            if pointer / open_list[i] <= Decimal('0.999'):
                if len(dict_tmp) == 0:
                    balance -= Decimal('10.0')
                    list_tmp = list(dict_tmp.keys())
                    try:
                        max_key = max(list_tmp) + 1
                    except ValueError:
                        max_key = 1
                    dict_tmp[max_key] = Decimal('10.0') / open_list[i]
                    
                for key, value in dict_tmp.items():
                    if value / open_list[i] <= Decimal('0.999'):
                        balance += value * open_list[i]
                        dict_tmp.pop(key)
                        break
            
            
            if pointer / open_list[i] >= Decimal('1.001'):
                balance -= Decimal('10.0')
                list_tmp = list(dict_tmp.keys())
                try:
                    max_key = max(list_tmp) + 1
                except ValueError:
                    max_key = 1
                dict_tmp[max_key] = Decimal('10.0') / open_list[i]
             
            pointer = open_list[i]
    
    price_tmp = open_list[len(open_list) - 1]
    open_list.clear()


value_tmp = Decimal('0.0')
for key, value in dict_tmp.items():
    value_tmp += value

print(balance)
print(value_tmp * price_tmp)