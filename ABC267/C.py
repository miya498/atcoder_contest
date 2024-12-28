N, M = map(int, input().split())
A = list(map(int, input().split()))

# 初期スコアを計算
current_score = 0
for i in range(M):
    current_score += (i + 1) * A[i]

max_score = current_score

# 現在の部分列の合計
current_sum = sum(A[:M])

# スライドウィンドウでスコアを更新
for i in range(M, N):
    current_score = current_score - current_sum + M * A[i]
    current_sum = current_sum - A[i - M] + A[i]
    max_score = max(max_score, current_score)

print(max_score)