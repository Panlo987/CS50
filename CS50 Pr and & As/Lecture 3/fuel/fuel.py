def read(n):
  num = int(n[0 : n.find('/')])
  den = int(n[n.find('/') + 1 : len(n) + 1])
  if num/den > 1:
    raise ValueError
  fuel = str(int((round(num / den, 2))*100)) + '%'
  if fuel in ['100%', '99%']:
    fuel = 'F'
  elif fuel in ['0%', '1%']:
    fuel = 'E'
  return fuel

def main():
  while True:
    try:
      print(read(input('Fraction: ')))
      break
    except ValueError:
      pass
    except ZeroDivisionError:
      pass

main()
