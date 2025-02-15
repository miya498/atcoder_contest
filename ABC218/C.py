N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

# 90度回転関数
def rotate(grid):
    return [list(row) for row in zip(*grid[::-1])]

# '#' の座標リストを取得
def get_positions(grid):
    return [(i, j) for i in range(N) for j in range(N) if grid[i][j] == "#"]

# 正規化 (左上のマスを原点にする)
def normalize(positions):
    if not positions:
        return set()
    min_x = min(x for x, y in positions)
    min_y = min(y for x, y in positions)
    return {(x - min_x, y - min_y) for x, y in positions}

# T の基準形を取得
T_positions = normalize(get_positions(T))

# S を 4 回回転しながらチェック
for _ in range(4):
    S_positions = normalize(get_positions(S))
    if S_positions == T_positions:
        print("Yes")
        exit()
    S = rotate(S)

print("No")
