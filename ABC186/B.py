H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

min_A = 101

for i in range(H):
    for j in range(W):
        if min_A > A[i][j]:
            min_A = A[i][j]

ans = 0
for i in range(H):
    for j in range(W):
        ans += A[i][j]-min_A

print(ans)
