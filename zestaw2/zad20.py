x, y = 123, 522

for base in range(2, 17):
    aDigits = [False for i in range(16)]
    bDigits = [False for i in range(16)]
    a = x
    b = y
    while a > 0:
        aDigits[a % base] = True
        a = a // base
        
    while b > 0:
        bDigits[b % base] = True
        b = b // base
    
    different = True
    for i in range(16):
        if aDigits[i] and bDigits[i]:
            different = False
    
    if different:
        print(base)
        exit()
    
print("None")