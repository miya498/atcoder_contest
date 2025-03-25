H,W = map(int,input().split())
grids = [list(input()) for _ in range(H)]

ans = [0 for _ in range(W)]
for i in range(H):
    for j in range(W):
        if grids[i][j] == "#":
            ans[j] += 1

print(*ans)
