T = [1,2,1,3,5,6,7,7,8,9,13,4]
def longestString(t):
    n = len(t)
    longest = 0
    
    for i in range(n-1):
        counter = 1
        sumNum = t[i]
        sumIndex = i
        if t[i] < t[i+1]:
            for j in range(i+1,n):
                if not t[j-1] < t[j]:
                    break
                else:
                    sumNum += t[j]
                    sumIndex += j
                    counter += 1
                    if sumNum == sumIndex:
                        longest = max(longest, counter)
                        
    return longest
    
print(T)
print(longestString(T))