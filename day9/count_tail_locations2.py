import sys

def update_tail(tlocation, hlocation):
    dx = hlocation[x] - tlocation[x]
    dy = hlocation[y] - tlocation[y]

    # h and t touching, don't move
    if abs(dx) <= 1 and abs(dy) <= 1:
        return tlocation

    # move t straight
    elif dy == 0 and 1 < abs(dx):
        # r
        if dx > 0:
            tlocation[x] += 1
        # l
        if dx < 0:
            tlocation[x] -= 1
    elif dx == 0 and 1 < abs(dy):
        # u
        if dy > 0:
            tlocation[y] += 1
        # d
        if dy < 0:
            tlocation[y] -= 1

    # move t diagonally
    else:
        # ur
        #. . . . .
        #. . h . .
        #. . . h .
        #. t . . .
        #. . . . .
        if (dy > 1 and dx == 1) or (dx > 1 and dy == 1):
            tlocation[x] += 1
            tlocation[y] += 1
        # ul
        #. . . . .
        #. . h . .
        #. h . . .
        #. . . t .
        #. . . . .
        elif (dy > 1 and dx == -1) or (dx < -1 and dy == 1):
            tlocation[x] -= 1
            tlocation[y] += 1
        # dr
        #. . . . .
        #. t . . .
        #. . . h .
        #. . h . .
        #. . . . .
        elif (dy < -1 and dx == 1) or (dx > 1 and dy == -1):
            tlocation[x] += 1
            tlocation[y] -= 1
        # dl
        #. . . . .
        #. . . t .
        #. h . . .
        #. . h . .
        #. . . . .
        elif (dy < -1 and dx == -1) or (dx < -1 and dy == -1):
            tlocation[x] -= 1
            tlocation[y] -= 1
        else:
            print('An error occured with update_tail')
            sys.exit(0)
    
    return tlocation
    



file = open('day9/input.txt')
tlocation = [0,0]
hlocation = [0,0]
tLocations = set()
x = 0
y = 1
for line in file:
    line = line.strip().split(' ')
    command = line[0]
    iterations = int(line[1])
    for _ in range(iterations):
        if command == 'R':
            hlocation[x] += 1
        elif command == 'L':
            hlocation[x] -= 1
        elif command == 'U':
            hlocation[y] += 1
        elif command == 'D':
            hlocation[y] -= 1
        update_tail(tlocation, hlocation)
        tLocations.add(tuple(tlocation))
    
print('The number of spaces visited is ' + str(len(tLocations)))