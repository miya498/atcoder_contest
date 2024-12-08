H, W, K = map(int, input().split())
S = [input().strip() for _ in range(H)]

# 移動方向の定義（上下左右）
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 深さ優先探索 (DFS) を使用してパスを数える
def count_paths(i, j, depth, visited):
    if depth == K:
        return 1  # K回の移動を達成したパスをカウント
    
    path_count = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '.' and (ni, nj) not in visited:
            visited.add((ni, nj))
            path_count += count_paths(ni, nj, depth + 1, visited)
            visited.remove((ni, nj))  # 戻るときに訪問済みを解除
    
    return path_count

# すべての空きマスを探索開始地点としてカウント
total_paths = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            total_paths += count_paths(i, j, 0, {(i, j)})

print(total_paths)