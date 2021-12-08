file = open('day8_inputs.txt')
input = []
for a in file:
    input.append( a[a.index('|') + 2:-1].split(' '))
print(input)
sum = 0
for a in input:
    for i in a:
        if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
            sum += 1
print(sum)