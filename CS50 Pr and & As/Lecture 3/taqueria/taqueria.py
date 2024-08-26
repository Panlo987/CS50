
menu = {"Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}

def price(input):
  if len(input) == 0:
    raise ValueError
  return menu[input]


def main():
  item = ' '
  total = 0.00
  while True:
    try:
      item = price(input('Item: ').title())
      total += item
      print('$' + str('%.2f' % total))
    except KeyError:
      pass
    except ValueError:
      break
    except EOFError:
      break

main()
