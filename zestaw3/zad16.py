def onlyOneMaxMin(t):
    n = len(t)
    maximum = 0
    minimum = 99999999999999
    maxCounter = 0
    minCounter = 0
    
    for i in range(n):
        if t[i] > maximum:
            maximum = t[i]
            maxCounter = 1
        elif t[i] == maximum:
            maxCounter += 1
        if t[i] < minimum:
            minimum = t[i]
            minCounter = 1
        elif t[i] == minimum:
            minCounter += 1
    
    return maxCounter == 1 and minCounter == 1
    
T = [2,4,5,7,8,12,6,1,12,13,13,5,20]
print(onlyOneMaxMin(T))