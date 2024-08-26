from jar import Jar
import pytest

def test_init():
  with pytest.raises(ValueError):
    j1 = Jar(-1) == ValueError

def test_str():
  j = Jar(20)
  j.deposit(5)
  assert str(j) == '🍪🍪🍪🍪🍪'
  j.deposit(3)
  assert str(j) == '🍪🍪🍪🍪🍪🍪🍪🍪'
  j.withdraw(6)
  assert str(j) == '🍪🍪'

def test_deposit():
  j = Jar()
  j.deposit(3)
  assert str(j) == '🍪🍪🍪'

def test_withdraw():
  j = Jar()
  j.deposit(6)
  j.withdraw(2)
  j.withdraw(1)
  assert str(j) == '🍪🍪🍪'
