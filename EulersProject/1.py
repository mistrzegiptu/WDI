sum = 0
for i in range(1000):
    if i % 15 == 0 or i % 5 == 0 or i % 3 == 0:
        sum += i
print(sum)