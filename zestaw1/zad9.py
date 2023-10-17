x = int(input())
i = 2
while i*i < x:

    if x%i == 0:
        print(i)
        print(x//i)
        
    i += 1
if i*i == x:
    print(i)
print(1)