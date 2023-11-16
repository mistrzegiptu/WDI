T = [[52,34,2,56], [78,75,14,10], [5,6,12,9], [10,53,21,8]]

def oneEvenEntireRow(t):
    n = len(t)
    
    for i in range(n):
    
        evenRow = True
        
        for j in range(n):
        
            l = t[i][j]
            evenDigit = False
            
            while l > 0:
                if l % 2 == 0:
                    evenDigit = True
                l = l // 10
            
            if not evenDigit:
                evenRow = False
                break
                
        if evenRow:
            return True
            
    return False
    
print(oneEvenEntireRow(T))