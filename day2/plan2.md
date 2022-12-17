```
lose = {A:C, B:A, C:B}
win = {A:B, B:C, C:A}

x : lose
y : tie
z : win


for every line in file
    if line[1] == 'x'
        total += points(lose(line))
    elif line[1] == 'y'
        total += 3 points(line[0])
    elif line[1] == 'z'
        total += 6 points(win(line))
print(total)

```
