# すべての 321-like Number を保持するリスト
ans = []

# 2進数の組み合わせを用いて、321-like Number を生成
for i in range(2, 1 << 10):
    x = 0
    for j in range(9, -1, -1):
        if i & (1 << j):
            x = x * 10 + j
    ans.append(x)

# 昇順にソート
ans.sort()

# 入力の受け取り
k = int(input())

# K 番目の 321-like Number を出力
print(ans[k - 1])