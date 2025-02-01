from collections import deque

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

start = None
goal = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)
v = [(-1, 0), (1, 0)]
h = [(0, -1), (0, 1)]

def bfs(start, first, sec):
    queue = deque([(start[0], start[1], 0)])  
    visited = [[[False] * 2 for _ in range(W)] for _ in range(H)]
    visited[start[0]][start[1]][0] = True

    while queue:
        x, y, ans = queue.popleft()

        if (x, y) == goal:
            return ans

        if ans % 2 == 0:
            next_moves = first
        else:
            next_moves = sec

        for dx, dy in next_moves:
            nx, ny = x + dx, y + dy
            if (0 <= nx < H) and (0 <= ny < W) and not visited[nx][ny][(ans + 1) % 2] and grid[nx][ny] != '#':
                visited[nx][ny][(ans + 1) % 2] = True
                queue.append((nx, ny, ans + 1))

    return float('inf')

result1 = bfs(start, v, h)
result2 = bfs(start, h, v)

result = min(result1, result2)
if result != float("inf"):
    print(result)
else:
    print(-1)