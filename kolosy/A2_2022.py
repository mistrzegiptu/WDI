'''1,3,2,4,6
   3,2,4,5,6
   2,1,5,6,5
   9,3,4,3,9
   4,5,6,7,4'''
t = [[1,3,2,4,6],[3,2,4,5,6],[2,1,2,6,5],[9,3,4,3,9],[4,5,6,7,4]]
def inSeq(n1, n2):
    a, b = 1, 2
    while a < n1 or b < n2:
        a, b = b, a+b-1
        
    return n1 == a and n2 == b
    
def seq(T):
    n = len(T)
    maxLength = 0
    
    for i in range(1,n-3):
        length = 2
        j = 0
        
        while j < n-3 and inSeq(t[i+j][j], t[i+j+1][j+1]) and t[i+j][j] + t[i+j+1][j+1] - 1 == t[i+j+2][j+2]:
            length += 2
            j += 1
        maxLength = max(length, maxLength)
    for i in range(1,n-3):
        length = 2
        j = 0
        
        while j < n-3 and inSeq(t[j][i+j], t[j+1][i+j+1]) and t[j][i+j] + t[j+1][i+j+1] - 1 == t[j+2][i+j+2]:
            length += 1
            j += 1
            
        maxLength = max(length, maxLength)
        
    k = 0
    length = 2
    
    while k < n-2 and inSeq(t[k][k], t[k+1][k+1]) and t[k][k] + t[k+1][k+1] - 1 == t[k+2][k+2]:
        length += 1
        k += 1
    maxLength = max(length, maxLength)
    
    return maxLength
    
print(seq(t))