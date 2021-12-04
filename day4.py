file = open('day4_inputs.txt')
inputs = file.readline()
cnt = 0
bingo = []
ans = []
for a in file:
    if a != '\n':
        bingo.append([a])
        cnt += 1

        if cnt == 5:
            print(bingo)
            bingo = []
            break
