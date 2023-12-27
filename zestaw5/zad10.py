def determinant(T):
    n = len(T)
    if n == 2:
        return T[0][0]*T[1][1] - T[0][1]*T[1][0]
    det = 0
    for remove in range(n):
        newT = [[0 for _ in range(n-1)] for _ in range(n-1)]
        skip = False
        for i in range(n-1):
            for j in range(n-1):
                if i == remove:
                    skip = True
                if skip:
                    newT[i] = T[i+1]
                else:
                    newT[i] = T[i]
        det = det + T[remove][n-1] * (-1)**(remove+n-1) * determinant(newT)
    return det

T = [
    [0,1,2,7],
    [1,2,3,4],
    [5,6,7,8],
    [-1,1,-1,1]
]
t = [[1,2,3,4,5],[0,2,3,4,5],[0,0,3,4,5],[0,0,0,4,5],[0,0,0,0,5]]
print(determinant(T))
print(determinant(t))