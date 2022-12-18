def find_priority(letter):
    if letter.isupper():
        ASCII_CONVERSION = 38
    if letter.islower():
        ASCII_CONVERSION = 96

    return ord(letter) - ASCII_CONVERSION


filename = 'input.txt'
file = open(filename)

total = 0
for line in file:
    line = line.strip()
    string_one = line[:int(len(line)/2)]
    string_two = line[int(len(line)/2):]
    print()

    print(f'The complete line : {line}')
    print(f'First half        : {string_one}')
    print(f'Second half       : {string_two}')
    
    for letter in string_one:
        if letter in string_two:
            print(f'Found match : {letter}')
            print(f'Match Score : {find_priority(letter)}')
            total = total + find_priority(letter)
            print(f'Total Score : {total}')
            break


print(total)
