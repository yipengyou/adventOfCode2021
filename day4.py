file = open('day4_inputs.txt')
inputs = file.readline()
cnt = 0
bingo = []
ans = []
d = {}
appended = False
for a in file:
    if a != '\n':
        
        temp = a[:-1].split(' ')
        
        for i in range(temp.count('')):
            temp.remove('')
        
        bingo.append(temp)
        cnt += 1

        if cnt == 5:
            for i in range(len(inputs)):
                for x in range(len(bingo)):
                    for y in range(len(bingo[x])):
                        if bingo[x][y] == inputs[i]:
                            bingo[x][y] = 'a'
                for w in bingo:
                    if w == []:
                        ans.append((i, inputs[i] * sum([q for e in bingo for q in e])))
                        appended = True
                        break
                if appended:
                    break
                else:
                    if len(bingo[0]) == 4 and len(bingo[1]) == 4 and len(bingo[2]) == 4 and len(bingo[3]) == 4 and len(bingo[4]) == 4:
                        ans.append(i, inputs[i] * sum([q for e in bingo for q in e]))
                        appended = True
                if appended:
                    break
            bingo = []
            cnt = 0
            appended = False
ans.sort()
print(ans)