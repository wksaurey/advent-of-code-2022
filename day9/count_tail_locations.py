# use grid system with starting point at (0,0)
# save tuple of location in set, then return set.len

def move_head_left():
    hx = hx-1

def move_head_right():
    hx = hx + 1

def move_head_up():
    hy = hy + 1

def move_head_down():
    hy = hy - 1

def check_tail():
    dx = hx - tx # change in x
    dy = hy - ty # change in y
    # touching, don't move
    if abs(dx) <= 1 and abs(dy) <= 1:
        return 

    # move straight
    elif dy == 0:
        # move left
        if dx == -2:
            ty = ty - 1
        # move right
        elif dx == 2:
            ty = ty + 1
    elif dx == 0:
        # move up
        if dy == 2:
            tx = tx + 1
        # move down
        elif dy == -2:
            tx = tx - 1

    # move diagonal
        # ul
        # ur
        # dr
        # dl
    pass

file = open("day9/input.txt")
hx = 0 # head x
hy = 0 # head y
tx = 0 # tail x 
ty = 0 # tail y
tLocations = set()
tLocations.add((tx, ty))
for line in file:
    line = line.strip().strip(' ')
    command = line[0]
    iterations = line[1] # amount of times to run command
    for _ in range(iterations):
        if command == 'L':
            move_head_left()
        elif command == 'R':
            move_head_right()
        elif command == 'U':
            move_head_up()
        else: #command == 'D'
            move_head_down()
        
        check_tail()
        
print('Number of Tail Locations : ' + str(len(tLocations)))


        

    
    