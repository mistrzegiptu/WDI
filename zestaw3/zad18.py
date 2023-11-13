t = [1,5,3,5,1,54,456,3,7,9,11,15,11,9,7,3]

def palindrom(T):
    n = len(T)
    maxLen = 0
    
    for i in range(1,n-1):
        if T[i] % 2 == 1:
            j = i-1
            k = i+1
            counter = 1
            
            while j >= 0 and k <= n-1:
                if T[j] % 2 == 0 or T[k] % 2 == 0:
                    break
                counter += 2
                j -= 1
                k += 1
            maxLen = max(maxLen, counter)
    
    return maxLen
    
print(palindrom(t))