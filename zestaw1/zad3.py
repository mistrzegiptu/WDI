suma = int(input())

a, b = 1, 1

while b < suma:
    a1 = b
    b1 = a - a1
    s = 0
    
    while b1 < suma:
        s += b1
        if s == suma:
            print(True)
            exit()
        c1 = a1
        a1 += b1
        b1 = c1
    
    c = a
    a += b
    b = c
print(False)