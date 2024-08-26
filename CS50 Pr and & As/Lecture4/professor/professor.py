import random

def main():
  level = get_level()
  errors = 0
  for n in range(10):
    errCount = 0
    answer = -1
    ans = -2
    num1 = generate_integer(level)
    num2 = generate_integer(level)
    ans = num1 + num2
    while answer != ans:
      try:
        answer = int(input(f'{num1} + {num2} = '))
      except ValueError:
        if answer != ans:
          print('EEE')
          errCount+=1
      if answer != ans:
        print('EEE')
        errCount+=1
      if errCount == 3:
        print(f'{num1} + {num2} = {ans}')
        errors+=1
        break
  score = 10 - errors
  print(f'Score: {score}')

def get_level():
  while True:
    try:
      n = int(input('Level: '))
      if n in [1, 2, 3]:
        break
      else:
        raise ValueError
    except ValueError:
      pass
  return n

def generate_integer(level):
  if level == 1:
    a = random.randint(0,9)
  elif level == 2:
    a = random.randint(10,99)
  else:
    a = random.randint(100,999)
  return a


if __name__ == "__main__":
    main()
