N = 5
T = [[0 for _ in range(N)] for _ in range(N)]

def move(T, row, col, i):
    n = len(T)
    X = [2, 1, -1, -2, -2, -1, 1, 2];
    Y = [1, 2, 2, 1, -1, -2, -2, -1];
    n_row = row + X[i]
    n_col = col + Y[i]
    if 0 <= n_row < n and 0 <= n_col < n and T[n_row][n_col] == 0:
        return (n_row, n_col)
def horse(T, row, col, counter = 1):
    n = len(T)
    T[row][col] = counter
    if counter == n*n:
        print(T)
    else:
        for i in range(8):
            if (r := move(T, row, col, i)) is not None:
                horse(T, r[0], r[1], counter+1)
        T[row][col] = 0

horse(T, 0, 0)