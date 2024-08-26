import sys
from PIL import Image, ImageOps

def main():
  if validLine(sys.argv):
    overlay(sys.argv[1], sys.argv[2])
    
def validLine(argv):
  try:
    if len(argv) < 3:
      sys.exit('Too few command-line arguments')
    elif len(argv) > 3:
      sys.exit('Too many command-line arguments')

    validFiles = ['jpeg', 'jpg', 'png']

    if argv[1].split('.')[1] not in validFiles:
      sys.exit('Invalid input')
    if argv[2].split('.')[1] not in validFiles:
      sys.exit('Invalid input')

    if argv[1].split('.')[1] != argv[2].split('.')[1]:
      sys.exit('Input and output have different extensions')

    return True

  except FileNotFoundError:
    sys.exit('File does not exist')
  except IndexError:
    sys.exit('Invalid input')

def overlay(inp, out):
  try:
    input = Image.open(inp)
    shirt = Image.open('shirt.png')
    input = ImageOps.fit(input, shirt.size)
    input.paste(shirt, shirt)
    input.save(out)
  except FileNotFoundError:
    sys.exit('Input does not exist')
  except OSError:
    sys.exit(1)

if __name__ == '__main__':
  main()
