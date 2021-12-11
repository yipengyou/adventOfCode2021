import time as t

inputs = open('day11_inputs.txt')

matrix = []
for a in inputs:
    matrix.append([int(i) for i in a if i != '\n'])
    
length = sum([len(i) for i in matrix])


def bfs(x,y, seen):
    if x >= 0 and x < len(matrix[0]) and y >= 0 and y < len(matrix) and [x,y] not in seen:
        matrix[y][x] += 1
        if matrix[y][x] == 10:
            bfs(x+1, y, seen + [[x,y]])
            bfs(x+1, y - 1, seen + [[x,y]])
            bfs(x+1, y + 1, seen + [[x,y]])
            bfs(x -1, y, seen + [[x,y]])
            bfs(x -1, y +1, seen + [[x,y]])
            bfs(x-1, y -1, seen + [[x,y]])
            bfs(x, y + 1, seen + [[x,y]])
            bfs(x, y -1, seen + [[x,y]])
        
        

ans = 0

while True:
    cnt = 0
    ans += 1
    
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            bfs(b, a, [])
    
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if matrix[a][b] > 9:
                cnt += 1
                matrix[a][b] = 0
    
    if cnt == length:
        break
print(ans)