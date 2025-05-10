from collections import deque

H,W = map(int,input().split())
S = [list(input().strip()) for _ in range(H)]

dist = [[-1]*W for _ in range(H)]
q = deque()

for i in range(H):
    for j in range(W):
        if S[i][j] == "E":
            dist[i][j] = 0
            q.append((i,j))

move = [(0,1),(1,0),(0,-1),(-1,0)]

while q:
    x,y = q.popleft()
    for dx,dy in move:
        nx,ny = x+dx,y+dy
        if 0 <= nx < H and 0 <= ny < W:
            if S[nx][ny] != "#" and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            d = dist[i][j]
            for dx,dy,arrow in [(-1, 0, '^'), (1, 0, 'v'), (0, -1, '<'), (0, 1, '>')]:
                nx,ny = i+dx,j+dy
                if 0 <= nx < H and 0 <= ny < W:
                    if dist[nx][ny] == d-1:
                        S[i][j] = arrow
                        break

for i in range(H):
    print("".join(S[i]))