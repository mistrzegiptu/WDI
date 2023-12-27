def waga(T, n):
    first = [0 for _ in range(len(T))]
    second = [0 for _ in range(len(T))]

    def rek(T, n, sum, i, choose):
        if choose == 1:
            second[i-1] = 0
            first[i-1] = T[i-1]
        elif choose == 2:
            first[i-1] = 0
            second[i-1] = T[i-1]
        if len(T) == i:
            if n == sum:
                return True
            return False
        if rek(T, n, sum, i+1, 0) or rek(T, n, sum+T[i], i+1, 1) or rek(T, n+T[i], sum, i+1, 2):
            return True
            
        if choose == 1:
            first[i-1] = 0
        elif choose == 2:
            second[i-1] = 0
            
        return False

    result = rek(T, n, 0, 0, 0)
    if result:
        print([x for x in first if x != 0])
        print([x for x in second if x != 0])
        
    return result

T = [2, 3, 5, 10, 12]
print(waga(T, 9))