N, M = map(int, input().split())

row_black = {}
row_white = {}
col_black = {}
col_white = {}

for _ in range(M):
    X, Y, C = input().split()
    X, Y = int(X), int(Y)

    if C == "B":
        if X in row_white and row_white[X] <= Y:
            print("No")
            exit()
        if Y in col_white and col_white[Y] <= X:
            print("No")
            exit()
        row_black[X] = max(row_black.get(X, 0), Y)
        col_black[Y] = max(col_black.get(Y, 0), X)

    elif C == "W":
        if X in row_black and row_black[X] >= Y:
            print("No")
            exit()
        if Y in col_black and col_black[Y] >= X:
            print("No")
            exit()
        row_white[X] = min(row_white.get(X, N + 1), Y)
        col_white[Y] = min(col_white.get(Y, N + 1), X)

print("Yes")