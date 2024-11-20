N, M, H, K = map(int, input().split())
S = input()
items = set(tuple(map(int, input().split())) for _ in range(M))

# 高橋君の初期位置と体力
current_x, current_y = 0, 0
current_health = H

# 方向の座標変化を定義
directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

for move in S:
    # 移動
    dx, dy = directions[move]
    current_x += dx
    current_y += dy
    current_health -= 1

    # 倒れる判定
    if current_health < 0:
        print("No")
        exit()

    # アイテムの利用
    if current_health < K and (current_x, current_y) in items:
        current_health = K
        items.remove((current_x, current_y))
print("Yes")