# use grid system with starting point at (0,0)
# save tuple of location in set, then return set.len

file = open("day9/input.txt")
hx = 0 # head x
hy = 0 # head y
tx = 0 # tail x 
ty = 0 # tail y
tLocations = set()
tLocations.add((tx, ty))

def move_head_left():
    global hx
    hx -= 1

def move_head_right():
    global hx
    hx += 1

def move_head_up():
    global hy
    hy += 1

def move_head_down():
    global hy
    hy -= 1

def check_tail():
    global hx
    global hy
    global tx
    global ty
    global tLocations
    dx = hx - tx # change in x
    dy = hy - ty # change in y
    # touching, don't move
    if abs(dx) <= 1 and abs(dy) <= 1:
        return 

    # move straight
    elif dy == 0:
        # move left
        if dx < 0:
            tx -= 1
        # move right
        elif dx > 0:
            tx += 1
    elif dx == 0:
        # move up
        if dy > 0:
            ty += 1
        # move down
        elif dy < 0:
            ty -= 1

    # move diagonal
    elif dy > 1:
        # uul
        if dx < 0:
            ty += 1
            tx -= 1
        # uur
        elif dx > 0:
            ty += 1
            tx += 1
    elif dy < -1:
        # ddl
        if dx < 0:
            ty -= 1
            tx -= 1
        # ddr
        elif dx > 0:
            ty += 1
            tx += 1
    elif dx < -1:
        # llu
        if dy < 0:
            tx -= 1
            ty += 1
        # lld
        elif dy > 0:
            tx -= 1
            ty -= 1
    elif dx > 1:
        # rru
        if dy < 0:
            tx += 1
            ty += 1
        # rrd
        if dy > 0:
            tx += 1
            ty -= 1
        
    tLocations.add((tx, ty))


for line in file:
    line = line.strip().split(' ')
    command = line[0]
    iterations = int(line[1]) # amount of times to run command
    for _ in range(iterations):
        if command == 'L':
            move_head_left()
        elif command == 'R':
            move_head_right()
        elif command == 'U':
            move_head_up()
        else: #command == 'D'
            move_head_down()

        answer = len(tLocations)
        check_tail()

        
print('Number of Tail Locations : ' + str(len(tLocations)))


        

    
    