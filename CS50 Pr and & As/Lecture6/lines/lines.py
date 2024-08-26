import sys
counter = 0
if len(sys.argv) == 2:
  if sys.argv[1].find('.py') >= 0:
    with open(sys.argv[1]) as file:
      list = file.readlines()
      while True:
        try:
          for line in list:
            if not(len(line.strip()) < 1 or line == '\n' or line.strip().startswith('#')):
              counter+=1
          break
        except ValueError:
          pass
      print(counter)
  else:
    print('Not a Python file')
    sys.exit(1)
elif len(sys.argv) < 2:
  print('Too few command-line arguments')
  sys.exit(1)
else:
  print('Too many command-line arguments')
  sys.exit(1)


