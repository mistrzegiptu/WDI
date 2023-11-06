conversion = { 
    10 : "A", 
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F"
}

def commonDigit(s1, s2):
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                return True
    
    return False
    
def convertNum(n, base):
    result = ""
    
    while n > 0:
        if n % base > 9:
            result += conversion[n%base]
        else:
            result += str(n % base)
        n = n // base
        
    return result

a, b = 123, 522
    
for i in range(2, 17):
    aConv = convertNum(a, i)
    bConv = convertNum(b, i)
    if not commonDigit(aConv, bConv):
        print(i)
        exit()
    
print("None")