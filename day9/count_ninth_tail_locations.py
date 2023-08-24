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
        if (dy > 1 and dx >= 1) or (dx > 1 and dy >= 1):
            tlocation[x] += 1
            tlocation[y] += 1
        # ul
        #. . . . .
        #. . h . .
        #. h . . .
        #. . . t .
        #. . . . .
        elif (dy > 1 and dx <= -1) or (dx < -1 and dy >= 1):
            tlocation[x] -= 1
            tlocation[y] += 1
        # dr
        #. . . . .
        #. t . . .
        #. . . h .
        #. . h . .
        #. . . . .
        elif (dy < -1 and dx >= 1) or (dx > 1 and dy <= -1):
            tlocation[x] += 1
            tlocation[y] -= 1
        # dl
        #. . . . .
        #. . . t .
        #. h . . .
        #. . h . .
        #. . . . .
        elif (dy < -1 and dx <= -1) or (dx < -1 and dy <= -1):
            tlocation[x] -= 1
            tlocation[y] -= 1
        else:
            print('An error occured with update_tail')
            sys.exit(0)
    
    return tlocation
    



file = open('day9/input.txt')
segmentLocations = [[0, 0]] * 10
tLocations = set()
x = 0
y = 1
index = 2
for line in file:
    line = line.strip().split(' ')
    command = line[0]
    iterations = int(line[1])
    for _ in range(iterations):
        # update 'head' (segmentLocations[0])
        if command == 'R':
            segmentLocations[0][x] += 1
        elif command == 'L':
            segmentLocations[0][x] -= 1
        elif command == 'U':
            segmentLocations[0][y] += 1
        elif command == 'D':
            segmentLocations[0][y] -= 1
        # update each segment in chain
        for index, segment in enumerate(segmentLocations[1:]):
            update_tail(segment, segmentLocations[index-1])
        tLocations.add(tuple(segmentLocations[-1]))
    
print('The number of spaces visited is ' + str(len(tLocations)))