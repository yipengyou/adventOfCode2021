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
potential = [[0,0]]
def dik(x, y, cost):
<<<<<<< HEAD
    print(x, y, cave[y][x], cost)
    if [x,y] == [len(cave[0]) - 1, len(cave) - 1]:
        return
=======
    print(x, y)
>>>>>>> 68c1f92b1aac390402ed9d15ca8af868a0b63346
    visted.append((x,y))
    if [x,y] in potential:
        potential.remove([x,y])
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
<<<<<<< HEAD
        
    dik(min(temp)[1][0], min(temp)[1][1], min(temp)[0])
    
dik(0, 0, 0)
=======
    
    if not temp:
        return
    else:
        for a in temp:
            if [a[1][0], a[1][1]] not in visted:
                potential.append([a[1][0], a[1][1]])
        dik(min(temp)[1][0], min(temp)[1][1], cost + min(temp)[0])

while len(potential) > 0:

    dik(potential[0][0],potential[0][1], risk[(potential[0][0], potential[0][1])])
>>>>>>> 68c1f92b1aac390402ed9d15ca8af868a0b63346

print(risk[(len(cave[0]) - 1, len(cave) - 1)])