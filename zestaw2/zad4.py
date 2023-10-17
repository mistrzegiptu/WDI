n = int(input())

counter = 0
for i in range(1, n+1):
    while i%2 == 0:
        i = i//2
    while i%3 == 0:
        i = i//3
    while i%5 == 0:
        i = i//5
    if i == 1:
        counter += 1
        
print(counter)