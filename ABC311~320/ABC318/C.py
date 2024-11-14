# 入力の読み込み
N, D, P = map(int, input().split())
F = list(map(int, input().split()))

# 通常運賃を降順にソート（高い運賃から順にパスを適用するため）
F.sort(reverse=True)

# D日ごとにセットで周遊パスを適用する
for left in range(0, N, D):
    # 対象となるD枚の範囲を決定
    right = min(left + D, N)  # 最後の部分がD未満になることもあるため調整

    # D枚分の合計運賃を計算
    cost = sum(F[left:right])

    # 周遊パスを使った方が安ければ、通常料金をPに置き換え
    if cost > P:
        # 使われた通常料金を0にし、周遊パス料金Pに置き換える
        for i in range(left, right):
            F[i] = 0
        F[left] = P
    else:
        # D枚分の合計運賃が周遊パス料金以下であれば、それ以上の置き換えは不要
        break

# 全ての運賃を合計して、最小の総運賃を計算
ans = sum(F)
print(ans)