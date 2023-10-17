def NWD(a, b):
    while b != 0:
        c = b
        b = a%b
        a = c
    return a
    
a = int(input())
b = int(input())
c = int(input())

d = a*b//NWD(a, b)

e = c*d//NWD(c, d)

print(e)