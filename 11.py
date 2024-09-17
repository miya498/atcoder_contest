N = int(input())

T = [0]
X = [0]
Y = [0]

# N個の座標と時刻を受け取る
for i in range(N):
    t, x, y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

can = True

# 各ステップで移動が可能かを確認
for i in range(N):
    time_diff = T[i+1] - T[i]  # 時間の差
    distance = abs(X[i+1] - X[i]) + abs(Y[i+1] - Y[i])  # 移動距離（マンハッタン距離）
    
    # 時間が移動距離よりも小さい場合や、偶奇が一致しない場合は移動できない
    if time_diff < distance or time_diff % 2 != distance % 2:
        can = False
        break

# 結果を表示
if can:
    print("Yes")
else:
    print("No")