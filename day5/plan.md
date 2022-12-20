# Day 5
```
split input to crate file and instruction file

parse crate layout
use stack (first in, first out)
	use a list, using only append() and pop() (put the number at the end and remove from the end)
how much of a cheat is it to hardcode this part in? 
	not at all 

parse intructions
move [for loop range] from init stack number, end stack number
	example: move 2 from 1 to 3
		for x in range (2)
			value = list2.pop()
			list3.append(value)

for line in file
	iteration = null
	init_stack = null
	end_stack = null
	for word in line
		if digit
			if iteration != null
				iteration = int(word)
			elif init_stack != null
				init_stack = int(word)
			elif end_stack != null
				end_stack = int(word)
	for x in range(iteration):
		stacks[end_stack].append(stacks[init_stacks].pop())

for stack in stacks
	print(stack.pop)
		
			


crate print dunder?
no need to process visually
```
