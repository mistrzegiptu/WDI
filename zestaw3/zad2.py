a = int(input())
b = int(input())

aDigits = [0 for _ in range(10)]
bDigits = [0 for _ in range(10)]

while a > 0:
    aDigits[a % 10] += 1
    a = a // 10
    
while b > 0:
    bDigits[b % 10] += 1
    b = b // 10
    
for i in range(10):
    if aDigits[i] != bDigits[i]:
        print(False)
        
print(True)