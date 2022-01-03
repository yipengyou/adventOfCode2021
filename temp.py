hashtable = {}
ans = []
for a in queries:
    mag = int(a[1:])
    dir = a[0]
    
    if dir == '+':
        if mag in hashtable:
            hashtable[mag] += 1
        else:
            hashtable[mag] = 1
    else:
        if mag in hashtable:
            hashtable[mag] = 0
    
    for a in hashtable:
        if a + diff in  hashtable:
            ans.append(hashtable[a] + hashtable[a + diff])
            
return ans
        
            