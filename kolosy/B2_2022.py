'''1,3,2,4,6
   3,2,4,5,6
   2,1,5,6,5
   9,3,4,3,9
   4,5,6,7,4'''
t = [[3,5,3,4,6],[3,7,4,5,6],[2,1,2,6,5],[9,3,4,7,9],[4,5,6,7,4]]
def hasTwoFactorials(n):
    i = 2
    factors = 0
    while i <= n:
        if n % i == 0:
            factors += 1
        while n % i == 0:
            n = n // i
        i += 1
        
    return factors == 2
    
def square(T):
    n = len(T)
    minLen = 0
    for k in range(1,n-1):
        for i in range(n-k):
            for j in range(n-k):
                if hasTwoFactorials(T[i][j]*T[i+k][j]*T[i][j+k]*T[i+k][j+k]):
                    return (i, j, k)
                    
    return 0
    
print(square(t))