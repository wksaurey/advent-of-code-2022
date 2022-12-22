import sys

def duplicates(section):
    for x in range(len(section)):
        if section[x] in section[:x]:
            return True
    return False

file = open('input.txt')
UNIQUE_LEN = 14
for line in file:
    line.strip()
    for x in range(len(line)-UNIQUE_LEN -1):
        if not duplicates(line[x:x+UNIQUE_LEN]):
            print(x+UNIQUE_LEN)
            sys.exit(0)
