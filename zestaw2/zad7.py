n = int(input())

for i in range(1, n+1):
    if n % (i*i+i+1) == 0:
        print(i)
        exit()
print(False)