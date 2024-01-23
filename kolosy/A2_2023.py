def Check(T):
    N = len(T)
    i, j = 0, 0
    move = [1, 0]

    while 0 <= i+move[0] < N and 0 <= j+move[1] < N:
        i+=move[0]
        j+=move[1]
        if T[i][j] == '/':
            move[0], move[1] = -move[1], -move[0]
        elif T[i][j] == '\\':
            move[0], move[1] = move[1], move[0]
    
    return i == N and j == N - 1

def Change(ogrod, mirror):
    if ogrod[mirror[0]][mirror[1]] == '/':
        ogrod[mirror[0]][mirror[1]] = '\\'
    else:
        ogrod[mirror[0]][mirror[1]] = '/'

def napraw(ogrod):
    N = len(ogrod)
    mirrors = []
    for i in range(N):
        for j in range(N):
            if ogrod[i][j] != ' ':
                mirrors.append((i, j))
    
    def rek(i):
        if i == len(mirrors)-1:
            return
        mir = mirrors[i]
        Change(ogrod, mir)

        for j in range(i, len(mirrors)):
            Change(ogrod, mirrors[j])
            if Check(ogrod):
                return
            Change(ogrod, mirrors[j])
        
        Change(ogrod, mir)

        rek(i+1)
    
    rek(0)

garden = [[' ' for _ in range(5)] for _ in range(5)]
garden[3][0] = '\\'
garden[4][1] = '\\'
garden[1][3] = '\\'
garden[4][4] = '\\'

garden[1][1] = '/'
garden[3][3] = '/' 
'''garden[3][0] = '\\'
garden[1][3] = '/'
garden[1][4] = '\\'
garden[4][4] = '\\'


garden[3][3] = '/' '''
print(Check(garden))
print(garden)
napraw(garden)
print(garden)
print(Check(garden))