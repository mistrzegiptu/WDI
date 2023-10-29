def longestArithmetics(T):
    l = len(T)
    longest = 0
    counter = 0
    q = 0
    for i in range(l-1):
        if counter == 0:
            q = T[i+1]//T[i]
        if T[i+1]//T[i] == q:
            counter += 1
        else:
            if longest < counter:
                longest = counter

            counter = 0
    
    return max(longest, counter)+1

N = [1,3,9,27,81,2,4,8,16,32,64]
print(longestArithmetics(N))