def dfs(x, y, visited):
    # 終点に到達した場合
    if x == H - 1 and y == W - 1:
        return 1

    count = 0
    # 移動方向（右、下）
    for dx, dy in [(0, 1), (1, 0)]:
        nx, ny = x + dx, y + dy
        # マスが範囲内かつ未訪問の値なら進む
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] not in visited:
            visited.add(grid[nx][ny])  # 現在の値を訪問済みとして追加
            count += dfs(nx, ny, visited)  # 次のマスへ進む
            visited.remove(grid[nx][ny])  # 戻る際に訪問済みを解除

    return count

# 入力
H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

# DFS を開始
visited_set = set([grid[0][0]])  # 初期位置を訪問済みとする
result = dfs(0, 0, visited_set)

# 結果を出力
print(result)