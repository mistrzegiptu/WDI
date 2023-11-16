T = [[52,34,2,56], [78,75,14,10], [5,6,12,9], [10,53,21,8]]

def sumRow(t, r):
    n = len(t)
    sum = 0
    for i in range(n):
        sum += t[r][i]
        
    return sum
    
def sumCol(t, c):
    n = len(t)
    sum = 0
    for i in range(n):
        sum += t[i][c]
        
    return sum
    
def maximum(t):
    n = len(t)
    maxQuotient = 1
    maxI = 0
    maxJ = 0
    
    for i in range(n):
        quotient = 1
        for j in range(n):
            quotient =  sumCol(t,j) / sumRow(t,i)
            
            if maxQuotient < quotient:
                maxQuotient = quotient
                maxI = i
                maxJ = j
           
    print(maxQuotient)
    return (maxI, maxJ)
    
print(maximum(T))