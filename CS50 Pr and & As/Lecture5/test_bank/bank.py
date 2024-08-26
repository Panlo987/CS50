def main():
  g = input('Greeting: ')
  print(f'${value(g)}')

def value(g):
  g = g.lower().strip()
  try:
    if g.find('hello') >= 0:
      return 0
    elif g[0] == 'h':
      return 20
    else:
      return 100
  except IndexError:
    return 100

if __name__ == '__main__':
  main()
