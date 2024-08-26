from um import count

def testDot():
  assert count('um...') == 1

def testMulti():
  assert count('hello, um, hello, um, world') == 2

def testFalse():
  assert count('yummy') == 0

def testFalseTwo():
  assert count('yummy umbar umbelicas treatum') == 0

def testCase():
  assert count('Um, hello, uM, world') == 2
