import sys


if __name__ == '__main__':

    sys.argv = ['', 'input.txt']

    results = {'AX':3, 'AY':6, 'AZ':0, 
               'BX':0, 'BY':3, 'BZ':6,
               'CX':6, 'CY':0, 'CZ':3}
    points = {'X':1, 'Y':2, 'Z':3}
    filename = sys.argv[1]
    file = open(filename)
    total = 0
    for line in file:
        line = line.strip().replace(' ', '')
        turn = 
        # print(line)
        print(results[line])
        print(points[line[1]])
        total = total + results[line] + points[line[1]]
    print(total)
