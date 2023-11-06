conversion = "0123456789ABCDEF"

n = int(input("Input number: "))
base = int(input("Input final base: "))
convertedNum = ""

while n > 0:
    convertedNum += conversion[n % base]
    n = n // base
    
print(convertedNum)