n = int(input())
a = 1

e = [0 for _ in range(n+1)]
s = [0 for _ in range(n+1)]

s[0] = 1
flag = True

while flag:
    p = 0
    for i in range(n, -1, -1):
        e[i] += s[i] + p
        p = e[i] // 10
        e[i] %= 10
        
    r = 0
    flag = False
    for i in range(n+1):
        s[i] += 10 * r
        r = s[i] % a
        s[i] //= a
        if s[i] > 0:
            flag = True
            
    a += 1

print(e[0], end='.')
for i in range(1, n):
    print(e[i], end='')