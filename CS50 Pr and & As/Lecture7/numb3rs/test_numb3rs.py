from numb3rs import validate
import sys

def testSingle():
  assert validate('0.0.0.0') == True

def testDouble():
  assert validate('00.19.99.40') == True

def testTriple():
  assert validate('111.255.249.199') == True

def testMix():
  assert validate('0.255.99.159') == True

def testRange():
  assert validate('0.256.256.256') == False
