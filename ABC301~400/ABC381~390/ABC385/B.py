H,W,X,Y = map(int,input().split())
grids = [input() for _ in range(H)]
T = list(input())

X -= 1
Y -= 1
ans = 0
visited = set()

for i in range(len(T)):
    if T[i] == "L":
        if Y > 0 and grids[X][Y-1] != '#':
            Y -= 1
    elif T[i] == "R":
        if Y < W-1 and grids[X][Y+1] != '#':
            Y += 1
    elif T[i] == "U":
        if X > 0 and grids[X-1][Y] != '#':
            X -= 1
    elif T[i] == "D":
        if X < H-1 and grids[X+1][Y] != '#':
            X += 1

    if grids[X][Y] == '@' and (X,Y) not in visited:
        ans += 1
        visited.add((X,Y))

print(X+1,Y+1,ans)