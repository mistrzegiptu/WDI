from math import log10

def function(a, b):
    aLen = int(log10(a)) + 1
    bLen = int(log10(b)) + 1
    aSplit = [0 for _ in range(aLen)]
    bSplit = [0 for _ in range(bLen)]
    i = aLen - 1
    while a > 0:
        aSplit[i] = a % 10
        a = a // 10
        i -= 1
    i = bLen - 1
    while b > 0:
        bSplit[i] = b % 10
        b = b // 10
        i -= 1

    print(aSplit)
    print(bSplit)

function(213, 456)