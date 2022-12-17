def find_priority(letter):
    if letter.isupper():
        ASCII_CONVERSION = 96
    if letter.islower():
        ASCII_CONVERSION = 64

    return ord(letter) - ASCII_CONVERSION

filename = input.txt
file = open(filename)

for line in file:
    string_one = line[:int(len(line)/2]
    string_two = line[int(len(line)/2):]
    
    for letter in string_one:
        if letter in string_two:
            total = total + find_priority(letter)


print(total)
