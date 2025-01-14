H,W = map(int,input().split())
grids = [input() for _ in range(H)]

koma_x = -1
koma_y = -1

for i in range(H):
    for j in range(W):
        if grids[i][j] == "o" and koma_x == -1:
            koma_x = i
            koma_y = j
        elif grids[i][j] == "o" and koma_x != -1:
            ans = abs(i-koma_x)+abs(j-koma_y)
            print(ans)
            exit()