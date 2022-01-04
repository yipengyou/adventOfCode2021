inputs = open('day15_inputs.txt')
cave = []
for a in inputs:
    cave.append([int(i) for i in a if i != '\n'])

risk = {}
for y in range(len(cave)):
    for x in range(len(cave[y])):
        risk[(x,y)] = float('inf')       
risk[(0,0)] = 0

cost = 0
x = 0
y = 0
ans = 0
while risk:
    if [x,y] == [99,99]:
        ans = risk[(99,99)]
    risk.pop((x,y))
    if not risk:
        break
    if x - 1 >= 0 and (x-1, y) in risk:
        risk[(x-1, y)] = min(risk[(x - 1, y)], cost + cave[y][x - 1])
        
    if x + 1 < len(cave[0]) and (x+ 1, y) in risk:
        risk[(x+1, y)] = min(risk[(x + 1, y)], cost + cave[y][x + 1])
        
    if y - 1 >= 0 and (x, y - 1) in risk:
        risk[(x, y - 1)] = min(risk[(x, y  -1 )], cost + cave[y - 1][x])
        
    if y + 1 < len(cave) and (x, y + 1) in risk:
        risk[(x, y + 1)] = min(risk[(x, y + 1)], cost + cave[ y + 1][x])

    temp = sorted(risk.items(), key = lambda item: item[1])[0]
    x = temp[0][0]
    y = temp[0][1]
    cost = temp[1]

print(ans)
