inputs = open('day13_inputs.txt')

matrix = []

maxx = 0
maxy = 0

grid = []
for a in inputs:
    maxx = max(int(a.split(',')[0]), maxx)
    maxy = max(int(a.split(',')[1]), maxy)
    matrix.append([int(i) for i in a.split(',')])

for a in range(maxy+1):
    grid.append([0 if [i, a] not in matrix else 1 for i in range(maxx+1)])


fold = open('day13_folding.txt')
folding = []
for a in fold:
    folding.append([a[a.index('=') - 1], int(a[a.index('=') + 1:])])


for a in folding:
    
    if a[0] == 'y':
        
        temp = grid[ - 1: a[1]: -1]
        grid = grid[:a[1]]
        diff = len(grid) - len(temp)
        
        for i in range(len(grid[diff:])):
            
            for _ in range(len(grid[i])):
                
                if grid[i][_] == 1 or temp[i-diff][_] == 1:
                    grid[i][_] = 1
                    
    else:
        temp = []
        for i in range(len(grid)):
            
            temp.append(grid[i][-1: a[1]: - 1])
            grid[i] = grid[i][:a[1]]
        
        diff = len(grid[0]) - len(temp[0])
        for i in range(len(grid)):
            
            for _ in range(len(grid[i][diff:])):
                if grid[i][_] == 1 or temp[i][_+diff] == 1:
                    grid[i][_] = 1

for a in grid:
    for b in a:
        if b == 1:
            print('$', end=' ')
        else:
            print(' ', end = ' ')
    print('\n')