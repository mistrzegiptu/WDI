def distance(a, b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))
def CalcCheckFields(board, N):
    counter = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                counter += 1

    return counter

def place(N, knights):
    T = [[0 for _ in range(N)] for _ in range(N)]
    CheckBoard = [[0 for _ in range(N)] for _ in range(N)]
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    checkCounter = 0
    maxCheckCounter = 0
    minDist = 10**10
    bestKnight = (0, 0)

    for knight in knights:
        T[knight[0]][knight[1]] = 1
        for move in moves:
            if 0 <= knight[0] + move[0] < N and 0 <= knight[1] + move[1] < N:
                CheckBoard[knight[0]+move[0]][knight[1]+move[1]] = 1
    
    checkCounter = CalcCheckFields(CheckBoard, N)

    def rek(i, j):
        nonlocal minDist, maxCheckCounter, bestKnight
        counter = 0
        if T[i][j] == 0:
            if distance((N//2, N//2), (i, j)) <= minDist:
                for move in moves:
                    if 0 <= i + move[0] < N and 0 <= j + move[1] < N and CheckBoard[i+move[0]][j+move[1]] == 0 and T[i+move[0]][j+move[1]] == 0:
                        counter += 1
                if(maxCheckCounter < checkCounter + counter):
                    maxCheckCounter = checkCounter + counter
                    bestKnight = (i, j)
            if i < N-1:
                rek(i+1, j)
            if j < N-1:
                rek(i, j+1)

    rek(0, 0)
    print(maxCheckCounter)
    print(bestKnight)

place(8, [(2, 1), (2, 5), (5, 1)])