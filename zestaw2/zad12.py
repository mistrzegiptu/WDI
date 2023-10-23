def digitEqualLength(n):
    n1 = n
    length = 0
    
    while n > 0:
        n = n // 10
        length += 1
    
    n = n1
    while n > 0:
        if n % 10 == length:
            return True
        n = n//10
        
    return False
    
l = int(input())
print(digitEqualLength(l))