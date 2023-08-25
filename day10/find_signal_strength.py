import sys

file = open('day10/input.txt')
cycleCount = 0
x = 1
testCycle = 20
dTestCycle = 40
signalStrength = 0

for line in file:
    line = line.strip().split(' ')
    command = line[0]
    if command == 'noop':
        cycleDelay = 1
    else:
        cycleDelay = 2
        dx = int(line[1])
    
    for cycle in range(cycleDelay):
        cycleCount += 1
        if cycleCount == testCycle:
            signalStrength += cycleCount * x
            print('Cycle ' + str(cycleCount) + ': ' + str(cycleCount * x))
            testCycle += dTestCycle
            if testCycle > 220:
                print('The signal strength is : ' + str(signalStrength))
                sys.exit(0)
    if command == 'addx':
        x += dx

print('The signal strength is : ' + str(signalStrength))