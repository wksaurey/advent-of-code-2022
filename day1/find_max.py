import sys

if __name__ == '__main__':
    sys.argv = ['day_one.py', 'input.txt']
    if len(sys.argv) < 2:
        print('Please input elf calorie file')
        exit(0)

    filename = sys.argv[1]

    file = open(filename)
    total = 0
    running_total = 0
    for line in file:
        line = line.strip()
        if line == '':
            if running_total > total:
                total = running_total
            running_total = 0
        else:
            number = int(line)
            running_total = running_total + number
    print(total)
