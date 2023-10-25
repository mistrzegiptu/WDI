def longestString(T):
    longest = 0
    length = 0
    
    for i in range(len(T)-1):
        if(T[i] < T[i+1]):
            length += 1
        else:
            if longest < length:
                longest = length
            
            length = 1
            
    return max(longest, length)
    
A = [1,2,3,4,8,4,5,6,1,2,4,5,6,7,8,9,10]
print(longestString(A))