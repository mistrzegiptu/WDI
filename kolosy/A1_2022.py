T = [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]

def sequence(t):
    n = len(t)
    
    for i in range(n-2):
        for j in range(i+2, n):
            q = t[j]//t[i]
            length = 0
            
            while j < n and t[i] * q == t[j]:
                i += 1
                j += 1
                length += 1
                
            if length > 2:
                return (i-length, i-1)
                
print(sequence(T))