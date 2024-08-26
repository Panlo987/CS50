import project

def testci(monkeypatch):
  inputs = iter(['250000', '6.5', '30'])
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))
  result = project.calcInterest()
  assert result == 'The total interest to be paid at the end of the mortgage will be $255089'

def testam(monkeypatch):
  inputs = iter(['250000', '6.5', '30'])
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))
  result = project.amortization()
  assert result == '$1264 is your monthly amortization'

def testbh(monkeypatch):
  inputs = iter(['2500'])
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))
  result = project.budgetHouse()
  assert result == 'A home with a value of $197803 or less\nwill cost less than half of your monthly salary'

