def czynniki(n):
    t = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            t.append(i)
            while n % i == 0:
                n = n // i
        
        i += 1
    
    return t
    
def arrayJumps(T):
    n = len(T)
    A = [False for _ in range(n)]
    A[0] = True
    
    for i in range(n):
        if A[i]:
            zb = czynniki(T[i])
        
        for j in zb:
            if i + j <= n-1:
                A[i+j] = True
                
    return A[n-1]
    
tab = [5,4,20,10,9,7]
print(arrayJumps(tab))