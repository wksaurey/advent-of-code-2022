import sys

if __name__ == '__main__':

    sys.argv = ['', 'input.txt']

    points = {'A':1, 'B':2, 'C':3}
    lose = {'A':'C', 'B':'A', 'C':'B'}
    win = {'A':'B', 'B':'C', 'C':'A'}
    filename = sys.argv[1]
    file = open(filename)
    total = 0
    for line in file:
        line = line.strip().replace(' ', '')
        if line[1] == 'X':
            total = total + points[lose[line[0]]]
        elif line[1] == 'Y':
            number = line[0]
            total = total + 3 + points[line[0]]
        elif line[1] == 'Z':
            total = total + 6 + points[win[line[0]]]
    print(total)
