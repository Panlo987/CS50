import validators

def checkEmail():
  inp = input('What is your email address? ')
  check = validators.email(inp)
  if check:
    return 'Valid'
  return 'Invalid'

def main():
  print(checkEmail())

if __name__ == '__main__':
  main()
