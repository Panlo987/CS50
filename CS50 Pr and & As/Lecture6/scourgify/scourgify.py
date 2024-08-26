import sys
import csv

if __name__ == '__main__':
  if len(sys.argv) == 3:
    try:
      with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        after = open(sys.argv[2], 'w')
        writer = csv.DictWriter(after, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for row in reader:
          name = row['name'].split(',')
          first = name[1].strip()
          last = name[0].strip()
          house = row['house']
          writer.writerow({'first' : first, 'last' : last, 'house' : house})
        after.close()
    except FileNotFoundError:
      print(f'Could not read {sys.argv[1]}')
      sys.exit(1)
  elif len(sys.argv) > 3:
    print('Too many command-line arguments')
    sys.exit(1)
  else:
    print('Too few command-line arguments')
    sys.exit(1)

#with open(sys.argv[1]) as file:
#        reader = csv.DictReader(file)
#        for row in reader:
#          print(row['name'].split(','))
