N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B の最大値を求める
K = max(B)

# id 配列を初期化 (-1 で埋める)
id = [-1] * (K + 1)

# 現在の美味しさの上限を K とする
r = K

# 美味しさごとに id を計算
for i in range(N):
    if A[i] <= r:
        # A[i] 以上 r 以下の寿司を人 i + 1 が取る
        for j in range(A[i], r + 1):
            id[j] = i + 1
        # r を更新
        r = A[i] - 1

# 残った寿司は誰も食べない
for j in range(1, r + 1):
    id[j] = -1

# クエリ B に応答
for b in B:
    print(id[b])