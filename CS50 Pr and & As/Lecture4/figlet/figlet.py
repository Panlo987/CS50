import sys
from pyfiglet import Figlet
figlet = Figlet()

def main():
  if len(sys.argv) == 2 or sys.argv[1] not in ['-f', '--font']\
  or sys.argv[2] not in figlet.getFonts():
    sys.exit(1)
  inp = input('Input: ')
  try:
    if sys.argv[1] in ['-f', '--font']:
      figlet.setFont(font=sys.argv[2])
    print('Output: ')
    print(figlet.renderText(inp))
  except IndexError:
    print(figlet.renderText(inp))

main()
