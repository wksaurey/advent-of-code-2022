import sys

if __name__ == '__main__':
    sys.argv = ['day_one.py', 'input.txt']
    if len(sys.argv) < 2:
        print('Please input elf calorie file')
        exit(0)

    filename = sys.argv[1]

    file = open(filename)
    
    elves = []
    running_total = 0
    for line in file:
        line = line.strip()
        if line == '':
            elves.append(running_total)
            running_total = 0
        else:
            number = int(line)
            running_total = running_total + number
    elves.sort(reverse=True)
    print(f'{elves[0] + elves[1] + elves[2]}')
