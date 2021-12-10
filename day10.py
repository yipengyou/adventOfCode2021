dicks = { ')': 3,
"]": 57,
'}': 1197,
'>': 25137 }

inputs = open("day10_inputs.txt")

stack = []
unfinished = []

sums = 0

###part1
for a in inputs:
    stack = []
    stack.append(a[0])
    if a[-1] == '\n':
        a = a[:-1]
    if stack:
        for i in a[1:]:
            if i == ']':
                if stack.pop(-1) != '[':
                    sums += dicks[i]
                    stack = []
                    break
            elif i == '}':
                if stack.pop(-1) != '{':
                    sums += dicks[i]
                    stack = []
                    break
            elif i == '>':
                if stack.pop(-1) != '<':
                    sums += dicks[i]
                    stack = []
                    break
            elif i == ')':
                if stack.pop(-1) != '(':
                    sums += dicks[i]
                    stack = []
                    break
            else:
                stack.append(i)
        if stack:
            unfinished.append(stack)

sums = []

dick = {'(':1,
        '[':2,
        '{':3,
        '<':4
        }


for a in unfinished:
    temp = 0
    for i in a[::-1]:
        temp *= 5
        temp += dick[i]
    sums.append(temp)
sums.sort()
print(sums[len(sums)// 2])
