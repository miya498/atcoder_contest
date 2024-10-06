import math
from itertools import permutations

# 入力を受け取る
N, S, T = map(int, input().split())

segments = []

# 各線分の始端と終端を処理
for _ in range(N):
    A, B, C, D = map(int, input().split())
    segments.append((A, B, C, D))

# 総合時間を計算する関数
def calculate_time(order, S, T):
    total_time = 0
    current_position = (0, 0)  # スタート位置

    for A, B, C, D in order:
        length = math.sqrt((C - A) ** 2 + (D - B) ** 2)
        draw_time = length / T

        move_time = math.sqrt((A - current_position[0]) ** 2 + (B - current_position[1]) ** 2) / S
        
        total_time += move_time + draw_time
        current_position = (C, D)  # 現在の位置を更新

    return total_time

# 最小時間を計算
min_time = float('inf')

for order in permutations(segments):
    time = calculate_time(order, S, T)
    min_time = min(min_time, time)

# 出力
print(min_time)
