R, G, B = map(int, input().split())

# 赤、緑、青のそれぞれの初期位置
red_pos = -100
green_pos = 0
blue_pos = 100

# 各色を1つの箱に集める
red_cost = R * abs(red_pos - (-100))  # 赤の移動
green_cost = G * abs(green_pos - 0)  # 緑の移動
blue_cost = B * abs(blue_pos - 100)  # 青の移動

# 合計操作回数
total_cost = red_cost + green_cost + blue_cost

print(total_cost)