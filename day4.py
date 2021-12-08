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
<<<<<<< HEAD
                    bingo[x] = [[] if y == inputs[i] else y for y in bingo[x]]
                    
=======
                    for y in range(len(bingo[x])):
                        if bingo[x][y] == inputs[i]:
                            bingo[x][y] = 'a'
>>>>>>> 259c5163faf72456b22da87302c94e1f4fd44f2c
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
<<<<<<< HEAD
print(ans[-1][1], inputs[ans[-1][0]])
=======
print(ans)
>>>>>>> 259c5163faf72456b22da87302c94e1f4fd44f2c
