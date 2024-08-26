from working import convert
import pytest

def testEnds():
  assert convert('1:59 AM to 11:59 PM') == '01:59 to 23:59'

def testZero():
  assert convert('1:00 AM to 8:00 PM') == '01:00 to 20:00'

def testNoZero():
  assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def testOffByOne():
  assert convert('9 AM to 5 PM') != '08:00 to 16:00'

def testOffByFive():
  assert convert('9:23 AM to 5:35 PM') != '09:18 to 17:30'

def testOmitsTo():
  with pytest.raises(ValueError):
    convert('9 AM 5 PM')

def testOutOfRange():
  with pytest.raises(ValueError):
    convert('9:60 AM to 5:00 PM')
