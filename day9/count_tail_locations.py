# use grid system with starting point at (0,0)
# save tuple of location in set, then return set.len

def move_head_left():
    pass

def move_head_right():
    pass

def move_head_up():
    pass

def move_head_down():
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
        


        

    
    