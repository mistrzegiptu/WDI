t = [0 for _ in range(10)]

while True:
    n = int(input())
    
    if n == 0:
        break
        
    for i in range(10):
        if n > t[i]:
            n, t[i] = t[i], n
            
print(t[-1])
    