a, b = 2, 1
sumEven = 0

while b < 4000000:
    if b%2 == 0:
        sumEven += b
    c = a
    a += b
    b = c
#end while
print(sumEven)