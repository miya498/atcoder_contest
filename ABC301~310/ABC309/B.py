N = int(input())
A = [input() for _ in range(N)]

B = [list(a) for a in A]

for i in range(N - 1):
    B[0][i + 1] = A[0][i]  # 上の辺
    B[N - 1][i] = A[N - 1][i + 1]  # 下の辺
    B[i + 1][N - 1] = A[i][N - 1]  # 右の辺
    B[i][0] = A[i + 1][0]  # 左の辺
for b in B:
    print(*b, sep="")