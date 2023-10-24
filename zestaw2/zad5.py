def nLen(n):
    counter = 0
    while n > 0:
        counter += 1
        n = n // 10
    
    return counter

a = 2315
aLen = nLen(a)
divisible = 0

for i in range(1, 2**(aLen)):
    a2 = a
    num = 0
    k = 0
    for j in range(0, aLen):
        if i % 2 == 1:
            num += (a2 % 10) * 10 ** k
            k += 1
        a2 = a2 // 10
        i = i // 2
    if num % 7 == 0:
        divisible += 1

print(divisible)