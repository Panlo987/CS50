ex = input('Expression: ').strip()
fnum = float(ex[0:ex.find(' ')])
op = ex[ex.find(' ') + 1]
lnum = float(ex[ex.find(op) + 2:])

if op == '+':
  print(fnum + lnum)
elif op == '-':
  print(fnum - lnum)
elif op == '*':
  print(fnum*lnum)
elif op == '/':
  print(fnum/lnum)
