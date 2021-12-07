import math as m
input = open('day7_inputs.txt')
input = input.readline()
input = input.split(',')

for a in range(len(input)):
    input[a] = int(input[a])
    
input.sort()

mid = m.ceil(sum(input) / len(input))
othermid = m.floor(sum(input)/ len(input))
# mid = (max(input) - min(input)) // 2

sums = 0
osum = 0

### part 1
for a in input:
    sums += a - mid

### part 2
for a in input:
    sums += sum([i for i in range(1, abs(a - mid) + 1)])
    osum += sum([i for i in range(1, abs(a - othermid) + 1)])

print(min(sums, osum))