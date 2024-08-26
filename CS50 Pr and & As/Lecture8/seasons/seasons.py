from datetime import date
from sys import exit
import inflect

p = inflect.engine()

def main():
  print(minutesSince(getDate(input('Date of birth: '))))

def getDate(inp):
  inp = inp.split('-')
  try:
    return date(int(inp[0]), int(inp[1]), int(inp[2]))
  except ValueError:
    exit('Invalid date')

def minutesSince(info):
  days = date.today() - info
  days = str(days).split(' ')[0]
  words = str(p.number_to_words(int(days) * 24 * 60)).capitalize()
  words = words.replace(' and', '')
  return words + ' minutes'


if __name__ == "__main__":
  main()
