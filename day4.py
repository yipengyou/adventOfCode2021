file = open('day4_inputs.txt')
inputs = file.readline()
inputs = inputs.split(',')
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
                    bingo[x] = [[] if y == inputs[i] else y for y in bingo[x]]
                    
                for w in bingo:
                    if w == [[], [], [], [], []]:
                        ans.append((int(i), int(inputs[i]) * sum([int(q) for e in bingo for q in e if type(q) == type('a')])))
                        appended = True
                        break
                    
                if appended:
                    break
                
                for a in range(5):
                    if bingo[0][a] == [] and bingo[1][a] == [] and bingo[2][a] == [] and bingo[3][a] == [] and bingo[4][a] == []:
                        ans.append((int(i), int(inputs[i]) * sum([int(q) for e in bingo for q in e if type(q) == type('a')])))
                        appended = True
                        break
                    
                if appended:
                    break
            bingo = []
            cnt = 0
            appended = False
print(file.read())
ans.sort()
print(ans[-1][1], inputs[ans[-1][0]])