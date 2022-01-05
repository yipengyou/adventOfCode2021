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


directions = [[-1, 1], [0, 1], [1, 1], [-1, 0], [0,0], [1, 0],   [ -1, -1],[0, -1] , [1, - 1] ]        
def process():
    newimage = []
    for i, a in enumerate(image):
        for j, b in enumerate(a):
            interest = [image[j + [k[0]]][i + k[1]] if j + k[0] in range(0, len(image[0])) and i + k[1] in range(0, len(image)) else '.' for k in directions)]
            interest = [1 if k == '#' else 0 for k in image]
            newimage.append(algo[interest])
    return newimage

for _ in range(2):
    image = process()
    
return 
        

