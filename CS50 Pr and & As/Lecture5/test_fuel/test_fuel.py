import pytest
from fuel import gauge
from fuel import convert

def testGauge():
  assert gauge(98) == '98%'
  assert gauge(99) == 'F'
  assert gauge(2) == '2%'
  assert gauge(1) == 'E'

def testConvert():
  assert convert('2/4') == 50
  assert convert('1/3') == 33
  with pytest.raises(ZeroDivisionError):
    convert('1/0')
  with pytest.raises(ValueError):
    convert('1.5/3')
