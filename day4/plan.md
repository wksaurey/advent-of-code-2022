# Section One
```
for line in file
    split line by comma
    elf one = first half
    elf two = second half

    if elf one max - min is bigger
        if elf two min and max in range of elf one
            overlap ++
    else 
        if elf one min and max in range of elf two
            overlap ++

print overlap
```
