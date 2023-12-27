from math import log10

def isMovingClose(w, k, wk, kk, move):
    return (w+move[0]-wk)**2 + (k+move[1]-kk)**2 < (w-wk)**2 + (k-kk)**2

def function(T, w , k):
    n = len(T)
    endingPoints = [(0, 0), (0, n-1), (n-1, 0), (n-1, n-1)]

    def moveKing(w, k, ec):
        wk = ec[0]
        kk = ec[1]
        if w == wk and k == kk:
            return True
        else:
            for m in [(1, 0), (1, 1), (0, 1), (-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1)]:
                if -1 < w + m[0] < n and -1 < k + m[1] < n and isMovingClose(w, k, wk, kk, m):
                    newValue = T[w+m[0]][k+m[1]]
                    if T[w][k] % 10 < newValue // (10**int(log10(newValue))):
                        if moveKing(w+m[0], k+m[1], ec):
                            return True
            return False

    for ep in endingPoints:
        if moveKing(w, k, ep):
            return True
    return False

T = [[5,1,1],[1,34,1],[1,1,21]]
print(function(T, 1, 1))