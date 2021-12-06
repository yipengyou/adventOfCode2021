import math as math
input = open('day6_inputs.txt')
dp = input.read()

dp = dp.split(',')
original = len(dp)
for a in range(len(dp)):
    dp[a] = int(dp[a])
    
# for _ in range(256):
#     for a in range(len(dp)):
#         dp[a] -= 1
#         if dp[a] == -1:
#             dp[a] = 6
#             dp.append(8)


d = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for a in dp:
    d[a] += 1 


for a in range(256):
    print(d)
    temp = 0
    for i in d:
        if i == 0:
            temp = d[0]
            d[0] = d[1]
            
        elif i == 6:
            d[5] = d[6]
            d[6] = d[7] + temp
        elif i == 8:
            d[7] = d[8]
            d[8] = temp      
        elif i == 7:
            pass
        else:
            d[i-1] = d[i]
            
print(sum([d[a] for a in d]))
    
