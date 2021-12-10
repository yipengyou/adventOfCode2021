dicks = { ')': 3,
"]": 57,
'}': 1197,
'>': 25137 }

inputs = open("day10_inputs.txt")

stack = []

sums = 0

###part1
for a in inputs:
    stack.append(a[0])
    if a[-1] == '\n':
        a = a[:-1]
    if stack:
        for i in a[1:]:
            if i == ']':
                if stack.pop(-1) != '[':
                    sums += dicks[i]
                    break
            elif i == '}':
                if stack.pop(-1) != '{':
                    sums += dicks[i]
                    break
            elif i == '>':
                if stack.pop(-1) != '<':
                    sums += dicks[i]
                    break
            elif i == ')':
                if stack.pop(-1) != '(':
                    sums += dicks[i]
                    break
            else:
                stack.append(i)
print(sums)