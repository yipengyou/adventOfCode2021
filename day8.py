file = open('day8_inputs.txt')
input = []
for a in file:
    input.append( a[a.index('|') + 2:-1].split(' '))
    
    
    
###part 1
# sum = 0
# for a in input:
#     for i in a:
#         if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
#             sum += 1
# print(sum)


###part 2
sums = 0
d = {
    ''.join(set('acedgfb')): 8,
    ''.join(set('cdfbe')): 5,
    ''.join(set('gcdfa')): 2,
    ''.join(set('fbcad')): 3,
    ''.join(set('dab')): 7,
    ''.join(set('cefabd')): 9,
    ''.join(set('cdfgeb')): 6,
    ''.join(set('eafb')): 4,
    ''.join(set('cagedb')): 0,
    ''.join(set('ab')): 1 }
for a in input:
    print(a)
    for i in a:
        sums += d[''.join(set(i))]
print(sums)