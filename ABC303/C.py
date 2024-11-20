N, M, H, K = map(int, input().split())
S = input()
items = {tuple(map(int, input().split())) for _ in range(M)}

# 高橋君の初期位置と体力
current_x, current_y = 0, 0
current_health = H

# 移動方向の定義
directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

def dfs(step, x, y, health):
    if health < 0:
        return False
    if step == N:
        return True

    # 次の移動
    dx, dy = directions[S[step]]
    nx, ny = x + dx, y + dy
    next_health = health - 1

    # アイテムがある場合
    if (nx, ny) in items and next_health < K:
        next_health = K
        items.remove((nx, ny))  # アイテムを消費

    # 再帰的に次の移動を試みる
    return dfs(step + 1, nx, ny, next_health)

# 結果の出力
if dfs(0, current_x, current_y, current_health):
    print("Yes")
else:
    print("No")