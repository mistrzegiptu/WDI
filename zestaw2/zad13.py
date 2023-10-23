def uniqeLastDigit(n):
    lastDigit = n % 10
    n = n//10
    while n > 0:
        if lastDigit == n % 10:
            return False
        n = n//10
    
    return True

l = int(input())
print(uniqeLastDigit(l))