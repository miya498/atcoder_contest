H,W,K = map(int,input().split())
grids = [list(input()) for _ in range(H)]
max_K = 0
for i in range(H):
    for j in range(W):
        if grids[i][j] == "#":
            max_K += 1
ans = 0
for bit_h in range(2**H):
    for bit_w in range(2**W):
        cnt = max_K
        for i in range(H):
            for j in range(W):
                if ((bit_h >> i) & 1) or ((bit_w >> j) & 1):
                    if grids[i][j] == "#":
                        cnt -= 1
        if cnt == K:
            ans += 1
print(ans)