
def convert(time):
  hours = float(time[0 : time.find(':')])
  mins = float(time[time.find(':') + 1 : len(time) + 1])
  mins = mins / 60
  time = hours + mins
  return time

def main():
  t = input('What time is it?: ')
  t = convert(t)
  if t >= 7 and t <= 8:
    print('breakfast time')
  elif t >= 12 and t <= 13:
    print('lunch time')
  elif t >= 18 and t <= 19:
    print('dinner time')
  return

if __name__ == "__main__":
  main()

