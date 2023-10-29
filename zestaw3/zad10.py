def longestArithmetics(T):
    l = len(T)
    longest = 0
    counter = 0
    r = 0
    for i in range(l-1):
        if counter == 0:
            r = T[i+1]-T[i]
        if T[i+1]-T[i] == r:
            counter += 1
        else:
            if longest < counter:
                longest = counter

            counter = 0
    
    return max(longest, counter)+1

N = [2,4,6,8,10,12,14,16,5,4,3,2,4,6,8,10,12,14]
print(longestArithmetics(N))