
minS = 9999999999999
minI = 9999999999999
for i in range(1, 1000):
    for j in range(1, 1000):
        b = i
        a = j
        while b <= 2023:
            if b == 2023:
                if minS > (i+j):
                    minS = i+j
                    minI = i
            c = a
            a += b
            b = c
            
print(minI, minS-minI)