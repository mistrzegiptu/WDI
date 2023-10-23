def digitAscending(n):
    ascending = True
    lastDigit = n%10
    n = n // 10
    
    while n > 0:
        if lastDigit <= n%10:
            ascending = False
            break;
        lastDigit = n%10
        n = n//10
    
    return ascending

n = int(input())
print(digitAscending(n))