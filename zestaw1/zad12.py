a = int(input())
b = int(input())
c = int(input())

while b != 0:
    d = b
    b = a%b
    a = d
while c != 0:
    d = c
    c = a%c
    a = d
print(a)