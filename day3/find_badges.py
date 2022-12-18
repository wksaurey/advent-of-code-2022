def find_priority(letter):
    if letter.isupper():
        ASCII_CONVERSION = 38
    if letter.islower():
        ASCII_CONVERSION = 96

    return ord(letter) - ASCII_CONVERSION


filename = 'input.txt'
file = open(filename)

total = 0
lines = file.readlines()
for group in range(0, len(lines), 3):
    line_1 = lines[group].strip()
    line_2 = lines[group + 1].strip() 
    line_3 = lines[group + 2].strip() 
   
    
    for letter in line_1:
        if letter in line_2 and letter in line_3:
            print(f'Found match : {letter}')
            print(f'Match Score : {find_priority(letter)}')
            total = total + find_priority(letter)
            print(f'Total Score : {total}')
            print()
            break


print(total)
