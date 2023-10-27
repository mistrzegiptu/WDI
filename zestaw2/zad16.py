def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    
    return sum
    
def sumFactors(n):
    n1 = n
    j = 2
    sum = 0
    while j <= n1//2:
        while n % j == 0:
            """if j == n1:
                sum = sumDigits(n1)+1"""
            sum += sumDigits(j)
            n = n // j
        
        j += 1
        
    return sum


for i in range(1, 1000000):
    if sumDigits(i) == sumFactors(i):
        print(i)