def emoji(w):
  if w.find(':)') >= 0:
    w = w.replace(':)', '🙂')
  if w.find(':(') >= 0:
    w = w.replace(':(', '🙁')
  return w

def main():
  word = input()
  print(emoji(word))

main()
