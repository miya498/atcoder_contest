import math

# 入力の受け取り
N, K = map(int, input().split())
A = list(map(int, input().split()))
zahyou = [tuple(map(int, input().split())) for _ in range(N)]

# 明かりを持つ人の座標を取得
light_positions = [zahyou[i - 1] for i in A]

# ユークリッド距離の計算
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 二分探索
left, right = 0, 10**9

while right - left > 1e-6:
    mid = (left + right) / 2
    covered = [False] * N
    
    # 明かりの範囲内にいる人をカバー
    for lx, ly in light_positions:
        for i in range(N):
            x, y = zahyou[i]
            if distance(lx, ly, x, y) <= mid:
                covered[i] = True

    # 全員がカバーされているか確認
    if all(covered):
        right = mid
    else:
        left = mid

# 結果の出力
print(right)