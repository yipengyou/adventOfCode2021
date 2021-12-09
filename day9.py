file = open('day9_inputs.txt')

matrix = []

for a in file:
    matrix.append([int(i)  for i in a if i != '\n'])

ans = []
seen = []

def dfs(x,y, seen):
    if [x,y] not in seen:
        seen.append([x,y])
        if x + 1 < len(matrix[0]) and matrix[y][x+1] <= matrix[y][x]:
            dfs(x + 1, y, seen)
        elif x - 1 >= 0 and matrix[y][x-1] <= matrix[y][x]:
            dfs(x-1, y, seen)
        elif y + 1 < len(matrix) and matrix[y+1][x] <= matrix[y][x]:
            dfs(x, y+1, seen)
        elif y - 1 >= 0 and matrix[y-1][x] <= matrix[y][x]:
            dfs(x, y-1, seen)
        else:
            ans.append(matrix[y][x])

for a in range(len(matrix)):
    for b in range(len(matrix[0])):
        if matrix[a][b] not in seen:
            dfs(b, a, seen)
print(ans)
print(sum([1+i for i in ans]))
