import os
import csv
import datetime

from decimal import Decimal


# file_path = 'E:\\R\\python_projects\\b_data\\data\\data_LTC'
file_path = 'F:\\data\\data_BCH'
file_list = os.listdir(file_path)
print(file_list)
data = []


for file in file_list:
    print(file)
    with open(os.path.join(file_path, file), newline='\n') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            data.append(Decimal(row[1]))


inevesting = 0
balance_coin = Decimal(0.0)

print('Start analyze')
for i in range(1, len(data)):
    inevesting += Decimal(1.0)
    balance_coin += Decimal(1.0) / data[i] * Decimal(0.999)
    
print('Finish analyze\n')

result = balance_coin * data[len(data)-1]
profit_percent = result / inevesting
print(f'Инвестировано: {inevesting}', f'Balance coin: {balance_coin}', f'Получено после продажи: {result}', f'Profit, %: {profit_percent}', sep='\n')
