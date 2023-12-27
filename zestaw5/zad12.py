def findN(T, result):
    n = len(T)
    counter = 0
    enki = [0 for _ in range(n)]

    def findN(i, product):
        nonlocal counter

        if n == i:
            if result == product:
                counter += 1
                print([x for x in enki if x != 0])
                return
        else:
            findN(i+1, product)
            enki[i] = T[i]
            findN(i+1, product*T[i])
            enki[i] = 0
    
    findN(0, 1)
    return counter

T = [1,2,3,4,5,6,8]
print(findN(T, 8))