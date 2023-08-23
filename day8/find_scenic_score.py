# import map of trees
file = open("day8/input.txt")
trees = []
for line in file:
    # tree_line = [int(x) for x in list(line.strip())]
    trees.append(line.strip())

# check if visible
def scenic_score(x, y, size):
    # check left
    tempx = x
    left_score = 0
    while tempx > 0:
        tempx -= 1
        left_score += 1
        if trees[y][tempx] >= trees[y][x]:
            break

    # check right
    tempx = x
    right_score = 0
    while tempx < size-1:
        tempx += 1
        right_score += 1
        if trees[y][tempx] >= trees[y][x]:
            break

    # check up
    tempy = y
    up_score = 0
    while tempy > 0:
        tempy -= 1
        up_score += 1
        if trees[tempy][x] >= trees[y][x]:
            break

    # check down
    tempy = y
    down_score = 0
    while tempy < size -1:
        tempy += 1
        down_score += 1
        if trees[tempy][x] >= trees[y][x]:
            break

    return left_score * right_score * up_score * down_score
        
# returns true if value is on edge of forest
def edge(x, y, size):
    return x == 0 or x == size-1 or y == 0 or y == size-1


# iterate through trees
max_score = 0
for y, line in enumerate(trees):
    for x, height in enumerate(line):
        if not edge(x, y, len(line)):
            score = scenic_score(x, y, len(line)) 
            if score > max_score:
                max_score = score

print("The highest scenic score is : " + str(max_score))