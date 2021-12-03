file = open('day3_inputs.txt')


###part 1 holy that took me a long time [[0,0]] * 12 makes a nested list of the same [0,0] dont do this in the future
# inputs = [[0,0] for a in range(12)]

for a in file:
    for i in range(len(a)):
        if a[i] == '1':
            inputs[i][1] += 1
        elif a[i] == '0':
            inputs[i][0] += 1
            
            
gamma = ['0' if a[0] > a[1] else '1' for a in inputs]
epsilon = ['0' if a[0] < a[1] else '1' for a in inputs]
print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))


###part 2 the first part does not work in sequence with part 2, comment out either part to run vice versa
















inputs = [a for a in file]
inputs2 = inputs.copy()

ones = 0
zeros = 0

pos = 0

potential = []

temp = ''




while len(inputs) != 1:
    
    zeros = 0
    ones = 0
    
    for a in inputs:
        if a[pos] == '1':
            ones += 1
        else: 
            zeros += 1
            
            
            
            
            
    if ones >= zeros:
        temp = '1'
    else:
        temp = '0'
        
        
        
        
        
    for a in inputs:
        if a[pos] == temp:
            potential.append(a)
            
            
            
    print(potential, pos)
    inputs = potential.copy()
    potential = []
    pos += 1

oxygenrating = int(inputs[0], 2)















ones = 0
zeros = 0
pos = 0
potential = []
temp = ''

while len(inputs2) != 1:
    
    zeros = 0
    ones = 0
    for a in inputs2:
        if a[pos] == '1':
            ones += 1
        else: 
            zeros += 1
    if ones >= zeros:
        temp = '0'
    else:
        temp = '1'
        
    for a in inputs2:
        if a[pos] == temp:
            potential.append(a)
            
    inputs2 = potential.copy()
    potential = []
    pos += 1

carbonrating = int(inputs2[0], 2)

print(carbonrating * oxygenrating)