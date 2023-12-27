from math import log10

def moveKing(T, w = 0, k = 0):
    n = len(T)
    if w == k == n - 1:
        return True
    else:
        flag = False
        for m in [(1, 0), (1, 1), (0, 1)]:
            if w + m[0] < n and k + m[1] < n:
                newValue = T[w+m[0]][k+m[1]]
                if T[w][k] % 10 < newValue // (10**int(log10(newValue))):
                    flag = flag or moveKing(T, w+m[0], k+m[1])
        return flag

T = [[11,1],[1,21]]
print(moveKing(T))