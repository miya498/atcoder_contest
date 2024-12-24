H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

# 各列の内容を収集
columns_s = ["".join(row[j] for row in S) for j in range(W)]
columns_t = ["".join(row[j] for row in T) for j in range(W)]

# ソートして比較
if sorted(columns_s) == sorted(columns_t):
    print("Yes")
else:
    print("No")
