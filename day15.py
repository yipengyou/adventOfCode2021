inputs = open('day15_inputs.txt')

cave = []
for a in inputs:
    cave.append([int(i) for i in a if i != '\n'])

risk = {}
for y in range(len(cave)):
    for x in range(len(cave[y])):
        risk[(x,y)] = float('inf')
risk[(0,0)] = 0

visted = []

def dik(x, y, cost):
    visted.append((x,y))
    temp = []
    if (x + 1, y) not in visted and (x+1, y) in risk:
        
        risk[(x+1,y)] = min(cost + cave[y][x+1], risk[(x+1, y)])
        temp.append((risk[(x+1, y)], (x+1,y)))
        
    if (x - 1, y) not in visted and (x-1, y) in risk:
        
        risk[(x-1,y)] = min(cost + cave[y][x-1], risk[(x-1, y)])
        temp.append((risk[(x-1,y)], (x-1,y)))
        
    if (x, y+1) not in visted and (x, y+1) in risk:
        
        risk[(x, y+1)] = min(cost + cave[y + 1][x], risk[(x, y+1)])
        temp.append((risk[(x, y+1)], (x, y+1)))
        
    if (x , y-1) not in visted and (x, y-1) in risk:
        
        risk[(x, y-1)] = min(cost + cave[y - 1][x], risk[(x, y-1)])
        temp.append((risk[(x,y-1)], (x, y-1)))
        
    dik(min(temp)[1][0], min(temp)[1][1], cost + min(temp)[0])
    
dik(0,0, 0)

print(risk[(len(cave[0]) - 1, len(cave) - 1)])