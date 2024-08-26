from plates import is_valid

def tests():
  assert is_valid('A1234') == False
  assert is_valid('A') == False
  assert is_valid('AB12345') == False
  assert is_valid('AAA9AA') == False
  assert is_valid('AAA.12') == False
  assert is_valid('123AAA') == False
  assert is_valid('AA0123') == False
