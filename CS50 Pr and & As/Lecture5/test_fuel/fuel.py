def main():
  while True:
    try:
      print(gauge(convert(input('Fraction: '))))
      break
    except ValueError:
      pass
    except ZeroDivisionError:
      pass

def gauge(percentage):
  fuel = str(percentage) + '%'
  if fuel in ['100%', '99%']:
    fuel = 'F'
  elif fuel in ['0%', '1%']:
    fuel = 'E'
  return fuel

def convert(fraction):
  num = int(fraction[0 : fraction.find('/')])
  den = int(fraction[fraction.find('/') + 1 : len(fraction) + 1])
  if num/den > 1:
    raise ValueError
  return int((round(num / den, 2))*100)

if __name__ == '__main__' :
  main()
