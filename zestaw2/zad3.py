l = int(input())

l1 = l
x = 0

while l > 0:
    x = x*10 + (l%10)
    l = l//10
print(x)
if l1 == x:
    print(True)
else:
    print(False)
    
bin1, bin2 = 0, 0

l = l1
counter = 0

while l > 0:
    bin1 = bin1 * 10 + l % 2
    if bin1 == 0:
        counter+=1
    l = l // 2
    
counter = 0
x = bin1
while x > 0:
    bin2 = bin2 * 10 + x % 10
    if bin2 == 0:
        counter+=1
    x = x // 10
    
bin1 = bin1*10**counter
bin2 = bin2*10**counter
print(bin1)
print(bin2)
if bin1 == bin2:
    print(True)
else:
    print(False)