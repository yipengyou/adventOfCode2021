file = 'day20_inputs.txt'
algo = ''
image = []
doingalgo = True
for i in open(file):
    if doingalgo:
        algo += i[:-1]
        if i == '\n':
            print('space')
            doingalgo = False
    else:
        if i[-1] == '\n':
            i = i[:-1]
        image.append([i])
    
print(algo, image)