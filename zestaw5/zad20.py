from math import log10

def isMovingClose(w, k, wk, kk, move):
    return (w+move[0]-wk)**2 + (k+move[1]-kk)**2 < (w-wk)**2 + (k-kk)**2

def function(T, w , k):
    n = len(T)
    endingPoints = [(0, 0), (0, n-1), (n-1, 0), (n-1, n-1)]
    moves = [(1, 0), (1, 1), (0, 1), (-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1)]
    M = [[-1 for _ in range(len(T))] for _ in range(len(T))]

    def moveKing(w, k, ec):
        wk = ec[0]
        kk = ec[1]
        if w == wk and k == kk:
            return True
        else:
            for i in range(len(moves)):
                if -1 < w + moves[i][0] < n and -1 < k + moves[i][1] < n and isMovingClose(w, k, wk, kk, moves[i]):
                    newValue = T[w+moves[i][0]][k+moves[i][1]]
                    if T[w][k] % 10 < newValue // (10**int(log10(newValue))):
                        if moveKing(w+moves[i][0], k+moves[i][1], ec):
                            M[w][k] = i
                            return True
            return False

    for ep in endingPoints:
        if moveKing(w, k, ep):
            for m in M:
                print(m)
            return True
    return False

T = [[5,1,1],[1,34,1],[1,1,21]]
print(function(T, 1, 1))