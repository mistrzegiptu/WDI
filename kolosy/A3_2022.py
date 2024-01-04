def longestKing(N, pawns):
    T = [[0 for _ in range(N)] for _ in range(N)]
    for pawn in pawns:
        T[pawn[0]][pawn[1]] = 2
    
    longestPath = 0

    def rek(i = 0, j = 0, currentLen = 0):
        nonlocal longestPath
        T[i][j] = 1
        if i == N - 1 and j == N - 1:
            longestPath = max(longestPath, currentLen)
            
        for move in [(1, 0), (-1, 0), (0, 1)]:
            if 0 <= i+move[0] < N and 0 <= j+move[1] < N and T[i+move[0]][j+move[1]] == 0:
                rek(i+move[0], j+move[1], currentLen+1)
        T[i][j] = 0

    rek()
    print(longestPath)

pawns = [(1, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 6)]
longestKing(8, pawns)