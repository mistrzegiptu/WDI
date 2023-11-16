T = [[52,34,2,55], [78,75,14,10], [5,6,12,9], [10,53,21,8]]

def oddInEveryRow(t):
    n = len(t)
    
    for i in range(n):
        odd = False
        for j in range(n):
            l = t[i][j]
            
            while (l % 10) % 2 == 1:
                l = l // 10
            
            if l == 0:
                odd = True
            
        if not odd:
            return False
            
    return True
    
print(oddInEveryRow(T))