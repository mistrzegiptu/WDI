def spiral(t):
    l = 1
    a = 0
    b = len(t)-1
    
    while a < b:
        for i in range(a, b):
            t[a][i] = l
            l += 1
            
        for i in range(a, b):
            t[i][b] = l
            l += 1
            
        for i in range(b, a, -1):
            t[b][i] = l
            l += 1
            
        for i in range(b, a, -1):
            t[i][a] = l
            l += 1
        
        a += 1
        b -= 1
        
    if len(t) % 2 != 0:
        t[len(t)//2][len(t)//2] = l
    for i in range(len(t)):
        for j in range(len(t)):
            print(t[i][j], end=" ")
        print()
        
N = int(input())
tab = [[0] * N for _ in range(N)]
spiral(tab)