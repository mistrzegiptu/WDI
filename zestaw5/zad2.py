tab = [2,4,7,15,18,22,3]

def Waga(n):
    i = 2
    counter = 0
    while i <= n:
        if n % i == 0:
            counter += 1
        while n % i == 0:
            n = n // i
        i+=1
    return counter

def function(T):
    n = len(T)
    def rek(i, a, b, c):
        if i == n:
            return a == b and b == c
        return rek(i+1, a+Waga(T[i]), b, c) or rek(i+1, a, b+Waga(T[i]), c) or rek(i+1, a, b, c+Waga(T[i]))
    
    return rek(0,0,0,0)

print(function(tab))