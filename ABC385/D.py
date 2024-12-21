from collections import defaultdict

N, M, Sx, Sy = map(int, input().split())


house_x = defaultdict(list)
house_y = defaultdict(list)
for _ in range(N):
    x, y = map(int, input().split())
    house_x[x].append(y)
    house_y[y].append(x)

moves = []
for _ in range(M):
    d, c = input().split()
    moves.append((d, int(c)))

visited = set()

for d, c in moves:
    if d == 'U':
        new_y = Sy + c
        for y in sorted(house_x[Sx]):
            if Sy < y <= new_y:
                visited.add((Sx, y))
        Sy = new_y
    elif d == 'D':
        new_y = Sy - c
        for y in sorted(house_x[Sx], reverse=True):
            if new_y <= y < Sy:
                visited.add((Sx, y))
        Sy = new_y
    elif d == 'L':
        new_x = Sx - c
        for x in sorted(house_y[Sy], reverse=True):
            if new_x <= x < Sx:
                visited.add((x, Sy))
        Sx = new_x
    elif d == 'R':
        new_x = Sx + c
        for x in sorted(house_y[Sy]):
            if Sx < x <= new_x:
                visited.add((x, Sy))
        Sx = new_x

print(Sx, Sy, len(visited))