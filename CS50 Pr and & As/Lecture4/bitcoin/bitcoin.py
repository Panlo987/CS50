import requests
import sys

try:
  bitc = float(sys.argv[1])
  if bitc > 0:
    price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    price = price['bpi']['USD']['rate']
    price = price.replace(',', '')
    price = float(price) * bitc
    print(f'${price:,.4f}')
  else:
    raise IndexError
except requests.RequestException or IndexError:
    print('Comman-line argument is not a number')
