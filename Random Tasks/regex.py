import re

RE = r'k..d..g....'

with open("../../../../Downloads/words.txt") as words:
    for line in words:
        if re.match(RE, line):
            print(line.strip())
