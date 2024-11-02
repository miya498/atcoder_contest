N = int(input())
A = list(map(int, input().split()))

# Bを求める
B = [-1] * N  # 初期値は全て -1 に設定
last_occurrence = {}  # 要素が最後に出現した位置を記録する辞書

for i in range(N):
    if A[i] in last_occurrence:
        B[i] = last_occurrence[A[i]]  # 最後に出現した位置をB[i]に代入
    last_occurrence[A[i]] = i + 1  # 現在の位置を記録（1-indexed）

# 結果を出力
print(*B)