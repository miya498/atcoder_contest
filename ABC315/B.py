# 入力の読み込み
M = int(input())
D = list(map(int, input().split()))

# 一年の真ん中の日の位置を計算
day = (sum(D) + 1) // 2

# 月ごとに日数を確認し、真ん中の日がどの月の何日かを見つける
for month in range(M):
    if day <= D[month]:
        # 現在の月で真ん中の日を見つけたので出力
        print(month + 1, day)
        break
    else:
        # 次の月へ移るため現在の月の日数を引く
        day -= D[month]