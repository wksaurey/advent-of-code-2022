def update_tail():
    pass


file = open('day9/test_input.txt')
tLocations = set()
for line in file:
    line = line.strip().split(' ')
    command = line[0]
    iterations = line[1]
    for _ in range(iterations):
        if command == 'L':
            pass
        elif command == 'R':
            pass
        elif command == 'U':
            pass
        elif command == 'D':
            pass
        update_tail()
    
print('The number of spaces visited is ' + str(len(tLocations)))