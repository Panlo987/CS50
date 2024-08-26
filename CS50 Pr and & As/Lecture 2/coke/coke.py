amountOwed = 50
coins = 0
while amountOwed > 0:
  print(f'Amount Due: {amountOwed}')
  coins = int(input('Insert coin: '))
  if coins in [25, 10, 5]:
    amountOwed -= coins
  print()
print(f'Change Owed: {abs(amountOwed)}')
