def main():
  names = []
  while True:
    try:
      names.append(input('Name: '))
    except EOFError:
      break
  if len(names) > 2:
    print('Adieu, adieu, to ', end='')
    for num in range(len(names) - 1):
      print(names[num] + ', ', end='')
    print('and ' + names[-1])
  else:
    print('Adieu, adieu, to ', end='')
    if len(names) == 1:
      print(names[0])
    else:
      print(f'{names[0]} and {names[1]}')

main()
