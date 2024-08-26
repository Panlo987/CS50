import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search('^([0-9]|[0-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])[.]([0-9]|[0-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])[.]([0-9]|[0-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])[.]([0-9]|[0-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])$', ip, re.IGNORECASE):
      return True
    return False


if __name__ == "__main__":
    main()
