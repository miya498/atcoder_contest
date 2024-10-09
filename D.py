# 時刻を5分単位に丸める関数
def round_time(t,flag):
    hour = t // 100
    minute = t % 100
    # 5分単位で丸める
    if minute % 5 != 0:
        if flag == 0:
            minute = (minute // 5) * 5 
        else:
            minute = (minute // 5) * 5 + 5
        if minute == 60:
            minute = 0
            hour += 1
    return hour * 100 + minute

# 入力の受け取り
N = int(input())
rain_intervals = []
for _ in range(N):
    S, E = input().split('-')
    S = round_time(int(S),0)
    E = round_time(int(E),1)
    rain_intervals.append((S, E))

# 開始時刻でソート
rain_intervals.sort()

# 結果を格納するリスト
result = []
start, end = rain_intervals[0]

for i in range(1, N):
    s, e = rain_intervals[i]
    if s <= end:  # 重なっている場合、endを更新
        end = max(end, e)
    else:
        # 重ならない場合は結果に格納し、新たな区間として開始
        result.append(f'{start:04d}-{end:04d}')
        start, end = s, e

# 最後の区間を結果に追加
result.append(f'{start:04d}-{end:04d}')

# 結果の出力
for r in result:
    print(r)