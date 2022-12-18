filename = 'input.txt'
file = open(filename)

overlap = 0
for line in file:
    line = line.strip()
    elf1 = line.split(',')[0]
    elf2 = line.split(',')[1]
    print(elf1)
    print(elf2)

    elf1_min = int(elf1.split('-')[0])
    elf1_max = int(elf1.split('-')[1])
    elf2_min = int(elf2.split('-')[0])
    elf2_max = int(elf2.split('-')[1])

    if elf1_max - elf1_min >= elf2_max - elf2_min:
        if elf1_max >= elf2_max and elf1_min <= elf2_min:
            overlap = overlap + 1
            print('yes')
    else:
        if elf2_max >= elf1_max and elf2_min <= elf1_min:
            overlap = overlap + 1
            print('yes')
    print(overlap)
    print()

print(overlap)
