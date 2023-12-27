def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n-1, A, C, B)
        print(A + " -> " + C)
        hanoi(n-1, B, A, C)

hanoi(64, "A", "B", "C")