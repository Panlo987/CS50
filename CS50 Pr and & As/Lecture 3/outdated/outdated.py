months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def checkDate(d):
  newd = d
  if d.find('/') >= 0:
    for char in d:
      if char.isnumeric():
        d = d.replace(char, '#')
  spl = d.split(' ')
  if d in ['#/#/####', '##/#/####', '#/##/####', '##/##/####']:
    sep = newd.split('/')
    month = sep[0]
    day = sep[1]
    year = sep[2]
    if int(day) > 31 or int(month) > 12:
      raise ValueError
    if len(sep[0]) == 1:
      month = '0' + sep[0]
    if len(sep[1]) == 1:
      day = '0' + sep[1]
    return f'{year}-{month}-{day}'
  elif spl[0].capitalize() in months and int(spl[2]) > 0:
    if spl[1].find(',') == -1:
      raise ValueError
    numMonth = str(months.index(spl[0]) + 1)
    if spl[0] not in months or int(spl[1].replace(',', '')) > 31:
      raise ValueError
    if len(numMonth) == 1:
      numMonth = '0' + numMonth
    if len(spl[1].replace(',', '')) == 1:
      spl[1] = '0' + spl[1]
    return f'{spl[2]}-{numMonth}-{spl[1].replace(",", "")}'
  else:
    raise ValueError

def main():
  while True:
    try:
      month = input('Date: ')
      print(checkDate(month.strip()))
      break
    except ValueError:
      pass
main()
