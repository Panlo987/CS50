def main():
  print("\033[H\033[J", end="")
  try:
    print('Welcome to the mortgage calculator! You can exit anytime by pressing Ctrl + D')
    print('-'*50)
    while True:
      c = choice()
      if c == 1:
        print(calcInterest())
      elif c == 2:
        print(amortization())
      elif c == 3:
        print(budgetHouse())
      else:
        pass
      while True:
        sc = input('Would you like to use the calculator again? (yes/no): ').lower()
        if sc == 'yes' or sc == 'no':
          break
        else:
          pass
      if sc == 'yes':
        print("\033[H\033[J", end="")
        pass
      else:
        break
    print("\033[H\033[J", end="")
    print('Thank you for using the Mortgage calculator!')
  except EOFError:
    print('Thank you for using the Mortgage calculator!')


def choice():
  while True:
    try:
      inp = int(input('Would you like to:\nCalculate interest (1)\nCalculate amortization\n(Amortization is paying off debt over time in equal installments.\nAs the term of your mortgage loan progresses,\na larger share of your payment goes toward paying\ndown the principal until the loan is paid in full\nat the end of your term.) (2)\nA budget for house shopping (3)\n'))
      break
    except ValueError:
      pass
  return inp


def calcInterest(): #returns how much interest will be paid at the end of the mortgage, assuming 20% down payment
  value = valueMortgage() * 0.8
  inter = valueInterest()
  term = valueTime()

  PMT = (value*(inter/12))/(1-(1/((1+(inter/12))**(12*term))))
  return f'The total interest to be paid at the end of the mortgage will be ${round((PMT*12*term) - value)}'


def amortization(): #returns the total amount paid at the end of the mortgage, assuming 20% down payment
  vm = valueMortgage() * 0.8
  inter = valueInterest()
  tm = valueTime()
  return f'${round((vm*(inter/12))/(1-(1/((1+(inter/12))**(12*tm)))))} is your monthly amortization'


def budgetHouse(): #returns the value of a house which costs under 50% of the users yearly income, assuming 6.5% interest
  print('This budget will assume an average of a 6.5% fixed interest and a 30-year loan')
  while True:
    try:
      income = int(input('What is your monthly income after taxes to the nearest single unit?: $'))
      break
    except ValueError:
      pass
  return f'A home with a value of ${round((income*0.5) * 158.2423)} or less\nwill cost less than half of your monthly salary'


def valueMortgage():
  while True: #Loop to ensure correct info is passed
    try:
      value = int(input('What is the value of the mortgage? (no periods or commas, rounded to the nearest single unit): '))
      return value
    except ValueError:
      pass

def valueInterest():
  while True: #Loop to ensure correct info is passed
    try:
      inter = float(input('What is the interest on the loan? (e.g. 12.63% interest = 12.63): '))
      return inter/100
    except ValueError:
      pass

def valueTime():
  while True: #Loop to ensure correct info is passed
    try:
      term = int(input('How long is the loan for in years?: '))
      return term
    except ValueError:
      pass

if __name__ == '__main__':
  main()
