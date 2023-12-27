def waga(T, n, sum = 0, i = 0):
    if len(T) == i:
        if n == sum:
            return True
        return False
    return waga(T, n, sum, i+1) or waga(T, n, sum+T[i], i+1)

T = [1, 2, 3, 5, 10, 12]
print(waga(T, 11))