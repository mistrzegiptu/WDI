def ile25(n):
    fiveCounter = 0
    twoCounter = 0
    
    while n % 2 == 0:
        twoCounter += 1
        n = n // 2
    
    while n % 5 == 0:
        fiveCounter += 1
        n = n // 5
        
    return max(fiveCounter, twoCounter)
    
def ulamek(l, m):
    r = 0
    print(l//m, end="")
    l = l % m
    
    if l == 0:
        return
    
    print(".", end="")
    
    for _ in range(ile25(m)):
        l *= 10
        print(l//m, end="")
        l = l % m
    
    if l == 0:
        return
        
    print("(", end="")
    r = l
    
    while True:
        l *= 10
        print(l//m, end="")
        l = l % m
        if l == r:
            print(")", end="")
            break
        
ulamek(1, 7)