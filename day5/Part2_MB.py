from collections import deque

# Create 9 deque collections to store letters in stacks
# stack_list contains d1 through d9
#TODO: Simplify - names are not necessary 
# since each deque is accessed only through its list index

nums = range(1,10)
d_rep = 'd'*9
stack_list = []

for d_i, num_i, in zip(d_rep, nums):
    label = d_i + str(num_i)
    label = deque()
    stack_list.append(label)

# Build stacks of cargo from input
with open("input05") as f:
    for line in f:
        if line[0] == '[':
            # Pull out contents of each crate
            line_items = line[1::4]
            for idx, item in enumerate(line_items):
                if item != ' ':
                    # Add item to stack, from left (bottom)
                    stack_list[idx].appendleft(item)
        elif line[0] == ' ':
            for stack in stack_list:
                print(stack)

#TODO: Try using rotate - could have a function input 
# for rotating vs. not rotating crane stack

with open("input05") as f:
    for line in f:
        if line[0:4] == 'move':
            instructions = line.split()
            num2pop      = int(instructions[1])
            from_stack_i = int(instructions[3])-1
            to_stack_i   = int(instructions[5])-1
            crane = deque()
            for item in range(0,num2pop):
                crane.append(stack_list[from_stack_i].pop())
            for item in range(0,num2pop):
                stack_list[to_stack_i].append(crane.pop())

for stack in stack_list:
    print(stack)

part2_solution = ''
for stack in stack_list:
    part2_solution = part2_solution + stack.pop()
    
print(part2_solution)