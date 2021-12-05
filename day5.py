input = open('day5_inputs.txt')
vert = []
hori = []
ans = []
for a in range(1000):
    ans.append([0 for b in range(1000)])
for a in input:
    print(a)