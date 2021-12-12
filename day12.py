inputs = open('day12_inputs.txt')

hash = {
    'start': 0,
    'end': -1
}

smallcaves = [0, -1]
temp = 1
for a in inputs:
    i = a.split('-')
    for _ in i:
        if '\n' in _:
            _ = _[:-1]
        if _ not in hash:
            if _.islower():
                smallcaves.append(temp)
            hash[_] = temp
            temp += 1


cave = [[] for _ in hash]

inputs = open('day12_inputs.txt')
for a in inputs:
    i = a.split('-')
    if '\n' in i[-1]:
        i[-1] = i[-1][:-1]
    cave[hash[i[0]]].append(hash[i[1]])
    cave[hash[i[1]]].append(hash[i[0]])

            
answer = []

def dfs(path, i, small):
    if i == -1:
        answer.append(path + [-1])
    elif i == 0:
        pass
    else:
        for a in cave[i]:
            if a in smallcaves and a in path:
                if not small:
                    dfs(path + [i], a, True)        
            else:
                dfs(path + [i], a, small)
                
for i in cave[0]:
    dfs([0], i, False)

print(len(answer))