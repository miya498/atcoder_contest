from collections import deque

# 入力の読み取り
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# 方向ベクトル（上下左右）
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# 訪問済みのマスを記録するための2次元リスト
visited = [[False] * W for _ in range(H)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == "#":
                visited[nx][ny] = True
                queue.append((nx, ny))

# 領域の数をカウントする
region_count = 0

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#" and not visited[i][j]:
            bfs(i, j)
            region_count += 1

print(region_count)
