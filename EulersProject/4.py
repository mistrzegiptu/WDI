def isPalindrome(n):
    n1 = n
    l = 0
    while n > 0:
        l = l * 10 + n%10
        n = n // 10
    return l == n1
largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(i*j):
            if largest < i*j:
                largest = i*j
                
print(largest)