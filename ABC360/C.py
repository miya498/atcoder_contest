N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

# 各 `A[i]` に対して、対応する最大の重みを保持する辞書を使用
max_weights = {}

for i in range(N):
    if A[i] not in max_weights:
        max_weights[A[i]] = W[i]
    else:
        max_weights[A[i]] = max(max_weights[A[i]], W[i])

# 総コストと最大重みの合計を計算
total_cost = sum(W)
max_cost = sum(max_weights.values())

# 結果を出力
print(total_cost - max_cost)