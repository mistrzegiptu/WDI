a = int(input())
b = int(input())
n = int(input())

print(a//b, end = ".")

for i in range(1, n+1):
    a = a%b * 10
    print(a//b, end = "")