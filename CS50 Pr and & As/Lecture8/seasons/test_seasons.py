from seasons import getDate
from seasons import minutesSince
import pytest

def test_input():
  with pytest.raises(TypeError):
    minutesSince(12-12-2012) == 'Invalid date'
