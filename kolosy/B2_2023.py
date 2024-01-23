def A(n):
    sum = 1
    i = 2
    while i < n:
        if n % i == 0:
            sum += i
        i += 1

    return sum

def B(n):
    a, b = 1, 1
    while b <= n:
        a, b = a+b, a
    
    return b

def C(n):
    rewers = 0
    num = n
    while num > 0:
        rewers = rewers * 10 + num % 10
        num = num // 10
    
    return rewers + n

def cycle(x, n):
    startingX = x
    steps = 0

    def rek(x, counter = 1):
        nonlocal steps

        if counter > n:
            return
        if x == startingX and counter != 1:
            steps = counter
            return
        rek(A(x), counter+1)
        rek(B(x), counter+1)
        rek(C(x), counter+1)
    
    rek(x, 1)
    return steps

print(cycle(29, 6))
'''print(A(6))
print(A(12))
print(A(17))
print(B(1))
print(B(4))
print(B(8))
print(C(1))
print(C(10))
print(C(13))'''