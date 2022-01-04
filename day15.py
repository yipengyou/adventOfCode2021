file = 'day15_inputs.txt'
cave = []

board_Pt2 = []

cpt = 0

board_width = 0

board_height = 0

row = []



for lines in open(file):
    
    while board_width < 5:

        temp_row = [x + cpt if x + cpt <= 9 else ((x + cpt + 1) % 10) for x in list(map(int," ".join(lines.replace("\n","")).split(" ")))]

        row += temp_row

        board_width += 1

        cpt += 1

    board_Pt2.append(row)

    row = []

    board_width = 0

    cpt = 0



final_board_Pt2 = []

final_board_Pt2[:] = board_Pt2[:] # Création d'une copie

cpt = 1

row = []

while board_height < 4: # 4 puisque nous avons déjà 1/5 de complété lorsque nous avons fait la largeur ci-haut

    for rows in board_Pt2:

        row = [x + cpt if x + cpt <= 9 else ((x + cpt + 1) % 10) for x in rows] # si x + cpt > 9 -> x + cpt + 1 % 10 (ex. (9 + 2) -> 11 + 1 -> 12 % 10 -> 2)

        final_board_Pt2.append(row)                                             # (9 + 1) -> 10 + 1 -> 11 % 10 -> 1

    board_height += 1

    cpt += 1
    
cave = final_board_Pt2

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
    if [x,y] == [len(cave[0]) - 1, len(cave) - 1]:
        ans = risk[len(cave[0]) - 1, len(cave) - 1]
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
