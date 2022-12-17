def find_priority(letter):
    if letter.isupper():
        ASCII_CONVERSION = 96
    if letter.islower():
        ASCII_CONVERSION = 64

    return ord(letter) - ASCII_CONVERSION


filename = 'input.txt'
file = open(filename)

total = 0
for line in file:
    string_one = line[:int(len(line)/2)]
    string_two = line[int(len(line)/2):]

    print(line)
    print(string_one)
    print(string_two)
    
    for letter in string_one:
        if letter in string_two:
            total = total + find_priority(letter)
            continue


print(total)
