file = open('day9_inputs.txt')

matrix = []

for a in file:
    matrix.append([int(i)  for i in a if i != '\n'])

ans = []

def dfs(x,y, seen):
    if [x,y] not in seen:
        if x + 1 < len(matrix[0]) and matrix[y][x+1] <= matrix[y][x]:
            dfs(x + 1, y, seen + [[x,y]])
        elif x - 1 >= 0 and matrix[y][x-1] <= matrix[y][x]:
            dfs(x-1, y, seen + [[x,y]])
        elif y + 1 < len(matrix) and matrix[y+1][x] <= matrix[y][x]:
            dfs(x, y+1, seen + [[x,y]])
        elif y - 1 >= 0 and matrix[y-1][x] <= matrix[y][x]:
            dfs(x, y-1, seen + [[x,y]])
        else:
            ans.append(matrix[y][x])
        matrix[x][y] = 'a'

for a in range(len(matrix)):
    for b in range(len(matrix[0])):
        if matrix[a][b] != 'a':
            dfs(b, a, [])

print(sum([1+i for i in ans]))
