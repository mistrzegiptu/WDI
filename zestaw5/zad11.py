def findN(T, result):
    n = len(T)
    counter = 0

    def findN(i, product):
        nonlocal counter

        if n == i:
            if result == product:
                counter += 1
                return
        else:
            findN(i+1, product)
            findN(i+1, product*T[i])
    
    findN(0, 1)
    return counter

T = [1,2,3,4,5,6]
print(findN(T, 6))