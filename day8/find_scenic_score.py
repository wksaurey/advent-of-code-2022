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
    isHidden = False
    while tempx > 0:
        tempx -= 1
        if trees[y][tempx] >= trees[y][x]:
            isHidden = True
    if not isHidden: return True

    # check right
    tempx = x
    isHidden = False
    while tempx < size-1:
        tempx += 1
        if trees[y][tempx] >= trees[y][x]:
            isHidden = True
    if not isHidden: return True

    # check up
    tempy = y
    isHidden = False
    while tempy > 0:
        tempy -= 1
        if trees[tempy][x] >= trees[y][x]:
            isHidden = True
    if not isHidden: return True

    # check down
    tempy = y
    isHidden = False
    while tempy < size -1:
        tempy += 1
        if trees[tempy][x] >= trees[y][x]:
            isHidden = True
    if not isHidden: return True

    # if isHidden from all sides, return false
    return False
        
# returns true if value is on edge of forest
def edge(x, y, size):
    return x == 0 or x == size-1 or y == 0 or y == size-1


# iterate through trees
max_score = 0
for y, line in enumerate(trees):
    for x, height in enumerate(line):
        score = scenic_score(x, y, len(line)) 
        if score > max_score:
            max_score = score

print("The number of visible trees (including edges) is : " + str(visible_sum))