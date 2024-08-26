g = input('Greeting: ').lower()
if g.find('hello') >= 0:
    print('$0')
elif g[0] == 'h':
    print('$20')
else:
    print('$100')
