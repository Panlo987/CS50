def main():
  plate = input("Plate: ")
  if is_valid(plate):
      print("Valid")
  else:
      print("Invalid")

def is_valid(s):
  s = s.upper()
  lastChar = ''
  error = 0
  for char in s:
    if (char == '0' and lastChar.isalpha()) or char in [' ', '.']:
      error += 1
    if lastChar.isnumeric() and char.isalpha() and s[s.find(char) + 1].isnumeric():
      error += 1
    lastChar = char
  if (s[-1].isnumeric() or s[-1].isalpha()) and s[0:2].isalpha() and len(s) <= 6 and len(s) >= 2 and error == 0:
    return True
  return False

if __name__ == '__main__':
  main()
