import os
import csv

from decimal import Decimal

coins = ['BTC', 'ETH', 'LTC', 'BCH']
file_path_main = 'E:\\R\\python_projects\\b_data\\data\\data_'
BTC_open_list_main = ETH_open_list_main = LTC_open_list_main = BCH_open_list_main = []

for coin in coins:
    data = []
    file_path = file_path_main + coin
    file_list = os.listdir(file_path)
    print(f'Loading {coin}')
    for file in file_list:
        with open(os.path.join(file_path, file), newline='\n') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                data.append(Decimal(row[1]))
    
    if coin == 'BTC':
        BTC_open_list_main = data
    elif coin == 'ETH':
        ETH_open_list_main = data
    elif coin == 'LTC':
        LTC_open_list_main = data
    elif coin == 'BCH':
        BCH_open_list_main = data
        
    print(f'Finish {coin}')


print(len(BTC_open_list_main), len(ETH_open_list_main), len(LTC_open_list_main), len(BCH_open_list_main), sep='\n', end='\n\n')


for j in range(5):
    BTC_open_list = BTC_open_list_main[j * 86400::]
    ETH_open_list = ETH_open_list_main[j * 86400::]
    LTC_open_list = LTC_open_list_main[j * 86400::]
    BCH_open_list = BCH_open_list_main[j * 86400::]
    # print(len(BTC_open_list), len(ETH_open_list), len(LTC_open_list), len(BCH_open_list), sep='\n', end='\n\n')
    
    flag_coin = 'ETH'
    pointer = 0
    balance = Decimal(1000.0)
    balance = balance / ETH_open_list[0]
    BTC_percent = ETH_percent = LTC_percent = BCH_percent = 0.0
    counter = 0

    print('Start analyze')
    for i in range(1, len(BTC_open_list)):
        BTC_percent = (BTC_open_list[pointer] / BTC_open_list[i]) - 1
        ETH_percent = (ETH_open_list[pointer] / ETH_open_list[i]) - 1
        LTC_percent = (LTC_open_list[pointer] / LTC_open_list[i]) - 1
        BCH_percent = (BCH_open_list[pointer] / BCH_open_list[i]) - 1
        
        flag_tmp = flag_coin
        
        if flag_coin == 'BTC':
            if BTC_percent > ETH_percent or BTC_percent > LTC_percent or BTC_percent > BCH_percent:
                flag_calc = False
                if BTC_percent > ETH_percent and abs(BTC_percent - ETH_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'ETH'
                    pointer = i
                    balance *= BTC_open_list[i]
                    balance /= ETH_open_list[i]
                    counter += 1
                elif BTC_percent > LTC_percent and abs(BTC_percent - LTC_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'LTC'
                    pointer = i
                    balance *= BTC_open_list[i]
                    balance /= LTC_open_list[i]
                    counter += 1
                elif BTC_percent > BCH_percent and abs(BTC_percent - BCH_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'BCH'
                    pointer = i
                    balance *= BTC_open_list[i]
                    balance /= BCH_open_list[i]
                    counter += 1
        elif flag_coin == 'ETH':
            if ETH_percent > BTC_percent or ETH_percent > LTC_percent or ETH_percent > BCH_percent:
                flag_calc = False
                if ETH_percent > BTC_percent and abs(ETH_percent - BTC_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'BTC'
                    pointer = i
                    balance *= ETH_open_list[i]
                    balance /= BTC_open_list[i]
                    counter += 1
                elif ETH_percent > LTC_percent and abs(ETH_percent - LTC_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'LTC'
                    pointer = i
                    balance *= ETH_open_list[i]
                    balance /= LTC_open_list[i]
                    counter += 1
                elif ETH_percent > BCH_percent and abs(ETH_percent - BCH_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'BCH'
                    pointer = i
                    balance *= ETH_open_list[i]
                    balance /= BCH_open_list[i]
                    counter += 1
        elif flag_coin == 'LTC':
            if LTC_percent > BTC_percent or LTC_percent > ETH_percent or LTC_percent > BCH_percent:
                flag_calc = False
                if LTC_percent > BTC_percent and abs(LTC_percent - BTC_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'BTC'
                    pointer = i
                    balance *= LTC_open_list[i]
                    balance /= BTC_open_list[i]
                    counter += 1
                elif LTC_percent > ETH_percent and abs(LTC_percent - ETH_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'ETH'
                    pointer = i
                    balance *= LTC_open_list[i]
                    balance /= ETH_open_list[i]
                    counter += 1
                elif LTC_percent > BCH_percent and abs(LTC_percent - BCH_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'BCH'
                    pointer = i
                    balance *= LTC_open_list[i]
                    balance /= BCH_open_list[i]
                    counter += 1
        elif flag_coin == 'BCH':
            if BCH_percent > BTC_percent or BCH_percent > ETH_percent or BCH_percent > LTC_percent:
                flag_calc = False
                if BCH_percent > BTC_percent and abs(BCH_percent - BTC_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'BTC'
                    pointer = i
                    balance *= BCH_open_list[i]
                    balance /= BTC_open_list[i]
                    counter += 1
                elif BCH_percent > ETH_percent and abs(BCH_percent - ETH_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'ETH'
                    pointer = i
                    balance *= BCH_open_list[i]
                    balance /= ETH_open_list[i]
                    counter += 1
                elif BCH_percent > LTC_percent and abs(BCH_percent - LTC_percent) > 0.02 and not flag_calc:
                    flag_calc = True
                    flag_tmp = 'LTC'
                    pointer = i
                    balance *= BCH_open_list[i]
                    balance /= LTC_open_list[i]
                    counter += 1
        
        flag_coin = flag_tmp

    print('Finish analyze')

    print(flag_coin, balance, counter, sep='\n', end='\n\n')
    
    with open('E:\\R\\python_projects\\b_data\\result.txt', 'a+') as f:
        f.writelines([flag_coin, '\n', str(balance), '\n', str(counter), '\n\n'])