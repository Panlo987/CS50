def main():
  inp = input('Input: ')
  print('Output:', shorten(inp.strip()))

def shorten(str):
  for v in str:
    if v.lower() in ['a', 'e', 'i', 'o', 'u']:
      str = str.replace(v, '')
  return str

if __name__ == "__main__":
  main()
