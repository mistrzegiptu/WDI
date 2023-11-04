def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    
    while n > 0:
        result *= n
        n -= 1
    
    return result
    
print(factorial(40)//(factorial(20)*factorial(20)))