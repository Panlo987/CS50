cc = input('Camel Case: ')

for cap in cc:
  if cap.isupper():
    cc = cc.replace(cap, '_' + cap.lower())

print(cc)
