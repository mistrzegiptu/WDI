n = int(input())

a = 2
while a <= n:
    if a % n == 0:
        print(True)
        exit()
    a = 3*a+1
    
print(False)