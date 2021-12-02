file = open('day2_inputs.txt', 'r')
inputs = {'forward':0, 'down':0, 'up':0}

#Part 1 and part 2 code can not be ran at the same time. comment out either section for the other section to function

###part 1
for a in file:
    temp = (a.split())
    inputs[temp[0]] += int(temp[1])
print(inputs['forward'] * (inputs['down'] - inputs['up']))

###part 2
aim = 0
depth = 0
for a in file:
    temp = a.split()
    if temp[0] == 'forward':
        inputs['forward'] += int(temp[1])
        depth += int(temp[1]) * aim
    elif temp[0] == 'up':
        aim -= int(temp[1])
    elif temp[0] == 'down':
        aim += int(temp[1])
print(inputs['forward'] * depth)
        