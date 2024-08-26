import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search('^<iframe (width="[0-9][0-9][0-9]" height="[0-9][0-9][0-9]" )?src="http(s)?://(www[.])?youtube[.]com/embed/([a-z0-9]+)"( title="[a-z0-9 ]+" frameborder="[0-9]" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)?></iframe>$', s.strip(), re.IGNORECASE)
    if matches:
        return f'https://youtu.be/{matches.group(4)}'
#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
#<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

if __name__ == "__main__":
    main()
