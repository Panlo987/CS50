import random
import sys

def rand(n):
  if n != 1:
    return int(random.randrange(1, n))
  else:
    return 1

def main():
  while True:
    try:
      n = int(input('Level: '))
      if n > 0:
        break
      else:
        raise ValueError
    except ValueError:
      pass
  r = rand(n)
  while True:
    while True:
      try:
        guess = int(input('Guess: '))
        break
      except ValueError:
        pass
    if guess == r:
      print('Just right!')
      sys.exit(1)
    elif guess < r:
      print('Too small!')
      pass
    else:
      print('Too large!')
      pass

main()
