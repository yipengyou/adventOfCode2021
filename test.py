f = open('day1_inputs.txt', 'r')
input = []
for a in f:
    input.append(int(a))

cnt = 0

#part1
last = input[0]
for a in input:
    if a > last:
        cnt += 1
    last = a




#part 2
prev = input[1]
prevprev = input[0]
last = input[2] + prev + prevprev

for a in input[2:]:
    if a + prev + prevprev > last:
        cnt += 1
    last = a + prev + prevprev
    prevprev = prev
    prev = a