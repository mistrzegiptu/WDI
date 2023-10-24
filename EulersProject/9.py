from math import sqrt

for i in range(1,1001):
    for j in range(1,1001):
        s = sqrt(i**2+j**2)
        if s - int(s) == 0:
            if i + j + int(s) == 1000:
                print(i, j, int(s))
                print(i*j*int(s))
            
print("dupa")