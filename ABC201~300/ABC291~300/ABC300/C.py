def dfs(grid, visited, x, y, H, W):
    # 4方向の移動ベクトル（右上、右下、左上、左下）
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    size = 0
    while True:
        size += 1
        for dx, dy in directions:
            nx, ny = x + dx * size, y + dy * size
            if not (0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '#' and not visited[nx][ny]):
                return size - 1
    return size - 1

def count_crosses(grid, H, W):
    visited = [[False] * W for _ in range(H)]
    cross_sizes = [0] * (min(H, W) + 1)
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                size = dfs(grid, visited, i, j, H, W)
                if size > 0:
                    cross_sizes[size] += 1
                    # 中心とその周囲を訪問済みにする
                    for d in range(size + 1):
                        for dx, dy in [(-d, -d), (-d, d), (d, -d), (d, d)]:
                            visited[i + dx][j + dy] = True
    
    # サイズ1からNまでの結果を出力
    result = cross_sizes[1:min(H, W) + 1]
    print(' '.join(map(str, result)))

# 入力の読み込み
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# クロスのカウント
count_crosses(grid, H, W)