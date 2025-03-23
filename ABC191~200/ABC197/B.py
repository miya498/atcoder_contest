H,W,X,Y = map(int,input().split())
grid = [list(input()) for _ in range(H)]

ans = 1
X -= 1
Y -= 1

for i in range(X-1,-1,-1):
    if grid[i][Y] == "#":
        break
    ans += 1

for i in range(X+1,H,1):
    if grid[i][Y] == "#":
        break
    ans += 1

for j in range(Y-1,-1,-1):
    if grid[X][j] == "#":
        break
    ans += 1

for j in range(Y+1,W,1):
    if grid[X][j] == "#":
        break
    ans += 1

print(ans)
