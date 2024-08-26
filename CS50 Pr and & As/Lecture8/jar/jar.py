class Jar:

  def __init__(self, capacity=12):
    if capacity < 0:
      raise ValueError
    self._capacity = capacity
    self.sz = 0

  def __str__(self):
    return f'{"🍪"*self.sz}'

  def deposit(self, n):
    if self._capacity - self.sz < n:
      raise ValueError
    if n > 0:
      self.sz += n

  def withdraw(self, n):
    if n <= self.sz:
      self.sz -= n
    else:
      raise ValueError

  @property
  def capacity(self):
    return self._capacity

  @property
  def size(self):
    return self.sz

j = Jar()
j.deposit(5)
print(j)
j.withdraw(3)
print(j)
