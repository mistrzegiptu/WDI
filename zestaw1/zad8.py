n = int(input())

i = 2
while i*i<=n:
    if n%i == 0:
        print(False)
        exit()
    i += 1
print(True)