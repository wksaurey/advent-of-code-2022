def printCrates():
    for stack in crates:
        for crate in stack:
            print(f'{crate} ', end='')
        print()
    print('\n')


crates = [
        ['T', 'D', 'W', 'Z', 'V', 'P'], 
        ['L', 'S', 'W', 'V', 'F', 'J', 'D'], 
        ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'], 
        ['R', 'S', 'J'], 
        ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'], 
        ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'], 
        ['V', 'J', 'P', 'C', 'B', 'D', 'N'], 
        ['P', 'T', 'B', 'Q'], 
        ['H', 'G', 'Z', 'R', 'C']
        ]


file = open('instructions.txt')
printCrates()
for line in file:
    iteration = -1
    init_stack = -1
    end_stack = -1
    words = line.strip().split(' ')
    for word in words:
        # print(word)
        if word.isdigit():
            if iteration == -1:
                # print('iteration')
                iteration = int(word) - 1
            elif init_stack == -1:
                # print('init')
                init_stack = int(word) - 1
            elif end_stack == -1:
                # print('end')
                end_stack = int(word) - 1
            else:
                print('Something went wrong while parsing instructions. A fourth number was detected.')
                exit(0)

    print(line, end='')
    printCrates()
    for x in range(iteration + 1):
        crates[end_stack].append(crates[init_stack].pop())
printCrates()
for stack in crates:
    if stack:
        print(stack.pop(), end='')
