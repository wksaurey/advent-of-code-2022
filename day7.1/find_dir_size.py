from tree import Node

root = Node('/', None, 0)
currentNode = root


file = open('day7.1/input.txt')
for line in file:
    line = line.strip().split(' ')
    if line[0] == '$':
        if line[1] == 'cd':
            # check for / and ..
            if line[2] == '/':
                currentNode = root
            elif line[2] == '..':
                currentNode = currentNode.get_parent()
            else:
                currentNode = currentNode.add_child(line[2])
    elif line[0] == 'dir':
        currentNode.add_child(line[1])
    else:
        # add size to currentNode and all parent nodes
        tempNode = currentNode
        while tempNode != None:
            tempNode.set_size(tempNode.get_size() + int(line[0]))
            tempNode = tempNode.get_parent()


# transverse tree, adding to a sum any value less than or equal to 100,000
def find_sum(root, maximum_size, sum):
    # if node.size is less than or equal to maximum size add to sum
    for child in root.get_children():
        sum = find_sum(child, maximum_size, sum)
    if root.get_size() <= maximum_size:
        sum += root.get_size()   
    return sum


print("Total of smaller directories : ", end='')
print(find_sum(root, 100000, 0))


space_needed = root.get_size() - 40000000

def clear_biggest_single_dir(root, space_needed, big_enough):
    for child in root.get_children():
        clear_biggest_single_dir(child, space_needed, big_enough)
    if root.get_size() >= space_needed:
        big_enough.append(root.get_size())
    return big_enough

big_enough = clear_biggest_single_dir(root, space_needed, [])
smallest = min(int(value) for value in big_enough)
print("Smallest = " + str(smallest))

