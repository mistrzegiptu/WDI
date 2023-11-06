def nthPowerSum(n, pow):
    result = 0
    n1 = n
    
    while n > 0:
        result += (n % 10)**pow
        n = n // 10

    return result == n1
    
N = int(input())

for i in range(10**(N-1), 10**N):
    if(nthPowerSum(i, N)):
        print(i)
        
print(nthPowerSum(153,3))