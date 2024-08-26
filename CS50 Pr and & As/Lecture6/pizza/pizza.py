import sys
from tabulate import tabulate

if len(sys.argv) == 2:
  if sys.argv[1].split('.')[1] == 'csv':
    try:
      with open(sys.argv[1]) as file:
        lines = file.readlines()
        headers = lines[0].strip()
        menu = []
        for line in lines[1:]:
          menu.append(line.split(','))
      print(tabulate(menu, headers=headers.split(','), tablefmt='grid'))
    except FileNotFoundError:
      print('File does not exist')
      sys.exit(1)
  else:
    print('Not a CSV file')
    sys.exit(1)
elif len(sys.argv) < 2:
  print('Too few command-line arguments')
  sys.exit(1)
else:
  print('Too many command-line arguments')
  sys.exit(1)


