from bank import value

def test():
  assert value('hello') == 0
  assert value('') == 100
  assert value('HELLO') == 0
  assert value('hey') == 20

