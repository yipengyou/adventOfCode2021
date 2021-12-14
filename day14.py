import collections as c
inputs = open('day14_inputs.txt')

initial = inputs.readline()[:-1]

initial = [i for i in initial]
dic = {}

whiteline = inputs.readline()   
for a in inputs:
    temp = a.split('->')
    temp[0] = temp[0][:-1]
    temp[1] = temp[1][1:]
    if temp[1][-1] == '\n':
        temp[1] = temp[1][:-1]
    
    dic[temp[0]] = [temp[0][0] + temp[1], temp[1] + temp[0][1]]
dics = {}
newdics = {}

for i in range(len(initial[:-1])):
    dics[initial[i] + initial[i+1]] = 1

counter = {}
for i in initial:
    if i not in counter:
        counter[i] = 1
    else:
        counter[i] += 1
            
for _ in range(40):
    for a in dics:
        
        if dic[a][0][1] not in counter:
            counter[dic[a][0][1]] = 1
        else:
            counter[dic[a][0][1]] += dics[a]
            
        if dic[a][0] not in newdics:
            newdics[dic[a][0]] = dics[a]
        else:
            newdics[dic[a][0]] += dics[a]
        if dic[a][1] not in newdics:
            newdics[dic[a][1]] = dics[a]
        else:
            newdics[dic[a][1]] += dics[a]
    dics = newdics
    newdics = {}

print(max(counter.values()) - min(counter.values()))
