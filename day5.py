input = open('day5_inputs.txt')
vert = []
hori = []
diag = []
ans = []
cnt = 0

for a in range(1000):
    ans.append([0 for b in range(1000)])

for a in input:
    
    start = a[:a.index(' ')]
    
    end = a[a.index('>') + 2:]
    
    p1 = start.split(',')
    p2 = end.split(',')
    
    if p2[-1][-1] == '\n':
        p2[-1] = p2[-1][:-1]
    
    if int(p1[0]) == int(p2[0]):
        if int(p1[1]) <= int(p2[1]):
            vert.append((p1,p2))
        else:
            vert.append((p2,p1))
            
    elif int(p1[1]) == int(p2[1]):
        if int(p1[0]) <= int(p2[0]):
            hori.append((p1, p2))
        else:
            hori.append((p2,p1))
    
    elif abs((int(p1[1]) - int(p2[1])) / (int(p1[0]) - int(p2[0]))) == 1:
        if int(p1[0]) <= int(p2[0]):
            diag.append((p1,p2))
        else:
            diag.append((p2,p1))
        
        


for a in hori:
    for i in range(int(a[0][0]), int(a[1][0]) + 1):
        if ans[int(a[0][1])][i] == 0:
            ans[int(a[0][1])][i] = '1'
        elif ans[int(a[0][1])][i] == '1':
            ans[int(a[0][1])][i] = 2
            
for a in vert:
    for i in range(int(a[0][1]), int(a[1][1]) + 1):
        if ans[i][int(a[0][0])] == 0:
            ans[i][int(a[0][0])] = '1'
        elif ans[i][int(a[0][0])] == '1':
            ans[i][int(a[0][0])] = 2
            
for a in diag:
    slope = (int(a[1][1]) - int(a[0][1])) // (int(a[1][0]) - int(a[0][0]))
    temp = 0
    for i in range(int(a[0][0]), int(a[1][0]) + 1):
        if ans[int(a[0][1]) + temp*slope][i] == 0:
            ans[int(a[0][1]) + temp*slope][i] = '1'
        elif ans[int(a[0][1]) + temp*slope][i] == '1':
            ans[int(a[0][1]) + temp*slope][i] = 2
        temp += 1
        

for a in ans:
    for b in a:
        if b == 2:
            cnt += 1 

print(cnt)