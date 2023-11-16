def sequence(T):
    n = len(T)
    counter = 1
    maxStart = 0
    minEnd = 10**10
    
    for i in range(n-1):
        if T[i] < T[i+1]:
            counter += 1
        else:
            if counter > 2:
                maxStart = max(maxStart, i-counter+1)
                minEnd = min(minEnd, T[i])
            
            counter = 1
            
    if counter > 2:
        maxStart = max(maxStart, i-counter+1)
        minEnd = min(minEnd, T[i])
        
    return minEnd < maxStart
    
t = [2,15,17,13,17,19,23,2,6,4,8,3,5,7,14,3,2]

print(sequence(t))