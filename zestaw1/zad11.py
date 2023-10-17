a = 2
while a <= 1000000:
    sum = 1
    i = 2
    while i*i < a:
    
        if a%i == 0:
            sum += i
            sum += (a//i)
            
        i += 1
    b = sum
    sum = 1
    i = 2
    while i*i < b:
    
        if b%i == 0:
            sum += i
            sum += (b//i)
            
        i += 1
    if sum == a and a != b:
        print(a, b)
    a += 1
    