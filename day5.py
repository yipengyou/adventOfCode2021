input = open('day5_inputs.txt')
vert = []
hori = []
ans = []
cnt = 0
for a in range(1000):
    ans.append([0 for b in range(1000)])
for a in input:
    start = a[:a.index(' ')]
    end = a[a.index('>') + 2:]
    p1 = start.split(',')
    p2 = end.split(',')
    if p1[0] == p2[0]:
        vert.append((p1,p2))
    elif p1[1] == p2[1]:
        hori.append((p1, p2))
for a in hori:
    for i in range(a[1]
    ans[a[0]] 