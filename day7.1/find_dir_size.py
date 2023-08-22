import sys
from tree import Node

root = Node('/', None, 0)
currentNode = root

file = open('input.txt')
for line in file:
    line = line.split(' ')
    if line[0] == '$':
        if line[1] == 'cd':
            # check for / and ..
            if currentNode.name == '/':
                currentNode = root
            if currentNode.name == '..':
                curentNode = currentNode.get_parent()
