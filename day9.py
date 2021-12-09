file = open('day9_inputs.txt')

matrix = []

for a in file:
    matrix.append([int(i)  for i in a if i != '\n'])

ans = []
seen = []

###part 1


def dfs(x,y):
    if [x,y] not in seen:
        seen.append([x,y])
        if x + 1 < len(matrix[0]) and matrix[y][x+1] <= matrix[y][x]:
            dfs(x + 1, y)
        elif x - 1 >= 0 and matrix[y][x-1] <= matrix[y][x]:
            dfs(x-1, y)
        elif y + 1 < len(matrix) and matrix[y+1][x] <= matrix[y][x]:
            dfs(x, y+1)
        elif y - 1 >= 0 and matrix[y-1][x] <= matrix[y][x]:
            dfs(x, y-1)
        else:
            ans.append([x,y])

for a in range(len(matrix)):
    for b in range(len(matrix[0])):
        if matrix[a][b] not in seen:
            dfs(b, a)
            

###part 2
basin = []
anss = []

def dfs2(x,y, seen):
    
    if [x,y] not in seen and matrix[y][x] != 9:
        
        if [x,y] not in basin: basin.append([x,y])
            
        if x + 1 < len(matrix[0]) and matrix[y][x+1] >= matrix[y][x] :
            
            dfs2(x + 1, y, seen + [[x, y]])
            
        if x - 1 >= 0 and matrix[y][x-1] >= matrix[y][x]:
            
            dfs2(x-1, y, seen + [[x, y]])
            
        if y + 1 < len(matrix) and matrix[y+1][x] >= matrix[y][x]:
            
            dfs2(x, y + 1, seen + [[x, y]])
            
        if y -1 >= 0 and matrix[y-1][x] >= matrix[y][x]:
            
            dfs2(x, y-1, seen + [[x, y]])

for a in ans:
    dfs2(a[0], a[1], [])
    anss.append(basin)
    basin = []

anss = sorted(anss, key=len)
print(len(anss[-1]) * len(anss[-2]) * len(anss[-3]))
        