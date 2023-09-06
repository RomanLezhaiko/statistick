import requests

response = requests.get('https://data.binance.vision/data/spot/monthly/klines/ADABKRW/1h/ADABKRW-1h-2020-08.zip')

with open('ADABKRW-1h-2020-08.zip', 'wb') as f:
    f.write(response.content)