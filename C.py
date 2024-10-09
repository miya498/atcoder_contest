# 入力の例
Deg, Dis = map(int, input().split())

# 角度を10分の1にして実際の角度に戻す
Deg = Deg / 10

# 風速を計算する
wind_speed = Dis / 60.0

# 風速を四捨五入して1桁の小数点に変更する
wind_speed = round(wind_speed + 0.005, 1)

# 方位と角度の対応表
directions = [
    "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
    "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
]

# 角度の境界
boundaries = [11.25, 33.75, 56.25, 78.75, 101.25, 123.75, 146.25, 168.75,
              191.25, 213.75, 236.25, 258.75, 281.25, 303.75, 326.25, 348.75]

# 方位を決定する関数
def get_direction(Deg):
    if Deg < 11.25 or Deg >= 348.75:
        return "N"
    for i in range(15):
        if boundaries[i] <= Deg < boundaries[i+1]:
            return directions[i+1]
    return "N"

# ビューフォート風力階級
def get_beaufort_scale(wind_speed):
    if wind_speed <= 0.2:
        return 0
    elif wind_speed <= 1.5:
        return 1
    elif wind_speed <= 3.3:
        return 2
    elif wind_speed <= 5.4:
        return 3
    elif wind_speed <= 7.9:
        return 4
    elif wind_speed <= 10.7:
        return 5
    elif wind_speed <= 13.8:
        return 6
    elif wind_speed <= 17.1:
        return 7
    elif wind_speed <= 20.7:
        return 8
    elif wind_speed <= 24.4:
        return 9
    elif wind_speed <= 28.4:
        return 10
    elif wind_speed <= 32.6:
        return 11
    else:
        return 12

# 風向と風力を取得
if wind_speed < 0.3:
    direction = "C"  # 風力0の場合は特別な向き "C"
else:
    direction = get_direction(Deg)

beaufort = get_beaufort_scale(wind_speed)

# 出力
print(direction, beaufort)
