* Read through file and find the block of calories that add up to the highest number. 

```
check if filename was input
set total to 0
read through every line in file
    if number, add to running_total
    if empty
        if running_total > total
            set total to running_total
        set running_total to 0
print total
```

```
check for filename
open file
set int[] elves
set elf to 0
set running_total to 0
for line in file
    line = line.strip()
    if line == ''
        elves[elf] = runnint_total
        elf = elf + 1
    else
        add number to running total
print total of first three elves
```
