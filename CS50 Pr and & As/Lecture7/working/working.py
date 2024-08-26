import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.match('^([1-9]|[1][012]?):?([0-5][0-9])? (AM|PM) to ([1-9]|[1][012]?):?([0-5][0-9])?( AM| PM)$', s)
    if matches:
        first = matches.group(1)
        second = matches.group(2)
        firstMeridian = matches.group(3)
        third = matches.group(4)
        fourth = matches.group(5)
        secondMeridian = matches.group(6)
        if firstMeridian == 'PM' and first != '12':
            first = int(first) + 12
            first = str(first)
        if secondMeridian == ' PM' and third != '12':
            third = int(third) + 12
            third = str(third)
        if int(first) < 10:
            first = '0' + first
        if int(third) < 10:
            third = '0' + third
        if second == None:
            second = '00'
        if fourth == None:
            fourth = '00'
        if firstMeridian == 'AM' and first == '12':
            first = '00'
        if secondMeridian == ' AM' and first == '12':
            third = '00'
    else:
        raise ValueError
    return f'{first}:{second} to {third}:{fourth}'





...


if __name__ == "__main__":
    main()
