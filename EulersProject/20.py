def factorial(n):
    if n == 0 or n == 1:
        return 1
        
    result = 1
    
    while n > 0:
        result *= n
        n -= 1
        
    return result
    
x = factorial(100)
sum =  0

while x > 1:
    sum += x % 10
    x = x // 10
    
print(sum)