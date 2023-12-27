def isLegal(T, x, y):
    sumW, sumK = 0, 0
    diagonalMoves = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

    for i in range(8):
        sumW += T[i][y]
        sumK += T[x][i]
    if sumK != 0 or sumW != 0:
        return False
    
    for move in diagonalMoves:
        i, j = x, y
        sum = 0
        while(-1<i<8 and -1<j<8):
            sum += T[i][j]
            i+=move[0]
            j+=move[1]
        if sum != 0:
            return False

    return True

def eightQueens():
    T = [[0 for _ in range(8)] for _ in range(8)]
    counter = 0
    def solve(i):
        nonlocal counter
        if i == 8:
            counter += 1
            for x in range(8):
                for y in range(8):
                    print(T[x][y], end = '')
                print()
            print()
        else:  
            for j in range(8):
                if isLegal(T, i, j):
                    T[i][j] = 1
                    solve(i+1)
                T[i][j] = 0

    solve(0)
    print(counter)

eightQueens()