H, W = map(int, input().split())

now_state_x = 0
now_state_y = 0

G = [list(input()) for _ in range(H)]
visited = set()

while True:
    if (now_state_x, now_state_y) in visited:
        print(-1)
        break

    visited.add((now_state_x, now_state_y))

    if G[now_state_x][now_state_y] == "U":
        if now_state_x == 0:
            print(now_state_x + 1, now_state_y + 1)
            break
        now_state_x -= 1
        continue
    if G[now_state_x][now_state_y] == "D":
        if now_state_x == H - 1:
            print(now_state_x + 1, now_state_y + 1)
            break
        now_state_x += 1
        continue
    if G[now_state_x][now_state_y] == "L":
        if now_state_y == 0:
            print(now_state_x + 1, now_state_y + 1)
            break
        now_state_y -= 1
        continue
    if G[now_state_x][now_state_y] == "R":
        if now_state_y == W - 1:
            print(now_state_x + 1, now_state_y + 1)
            break
        now_state_y += 1
        continue