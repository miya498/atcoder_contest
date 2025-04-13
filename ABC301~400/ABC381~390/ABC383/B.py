H,W,D = map(int,input().split())
grid = [input() for _ in range(H)]

floor = []

for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            floor.append((i, j))

ans = 0

for i in range(len(floor)):
    for j in range(i + 1,len(floor)):
        kashituki = set()
        x1, y1 = floor[i]
        x2, y2 = floor[j]
        
        for x in range(H):
            for y in range(W):
                if grid[x][y] == '.' and (abs(x - x1) + abs(y - y1) <= D or abs(x - x2) + abs(y - y2) <= D):
                    kashituki.add((x, y))
        
        ans = max(ans,len(kashituki))

print(ans)
