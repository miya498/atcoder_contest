H,W = map(int,input().split())

S = [input() for _ in range(H)]
target = "snuke"
direction = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

for i in range(H):
    for j in range(W):
        if S[i][j] == target[0]:
            for dx,dy in direction:
                ans = []
                x,y = i,j
                for k in range(5):
                    if 0 <= x < H and 0 <= y < W and S[x][y] == target[k]:
                        ans.append((x+1,y+1))
                        x += dx
                        y += dy
                    else:
                        break

                    if len(ans) == 5:
                        for q in range(5):
                            print(*ans[q])
                        exit()