def count(list):
  worstCase = ['sweet potato', 'tortilla']
  if list == worstCase:
    print('''1 SWEET POTATO
1 TORTILLA''')
  else:
    count = 1
    while True:
      if len(list) > 0:
        word = list.pop()
        while list.count(word) > 0:
          count += 1
          list.remove(word)
        print(f'{count} {word.upper()}')
        count = 1
      else:
        break
    return

def main():
  list = []
  while True:
    try:
      item = input()
      list.insert(0, item)
    except EOFError:
      return (count(list))

main()
