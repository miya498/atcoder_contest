N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

# グリッドを回転する関数
def rotate(grid):
    return [[grid[N - 1 - j][i] for j in range(N)] for i in range(N)]

# 条件を確認する関数
def is_valid(A, B):
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] != 1:
                return False
    return True

# 最大4回回転して確認
for _ in range(4):
    if is_valid(A, B):
        print("Yes")
        break
    A = rotate(A)
else:
    print("No")