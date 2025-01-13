N, K = map(int, input().split())
A = list(map(int, input().split()))

# 1. グループごとに分ける
groups = [[] for _ in range(K)]
for i in range(N):
    groups[i % K].append(A[i])

# 2. 各グループをソートする
for group in groups:
    group.sort()

# 3. 元の位置に戻して、新しい数列を作る
sorted_A = [0] * N
indices = [0] * K  # 各グループの取り出し位置を管理する配列

for i in range(N):
    group_index = i % K
    sorted_A[i] = groups[group_index][indices[group_index]]
    indices[group_index] += 1

# 4. 昇順になっているか判定
if sorted_A == sorted(A):
    print("Yes")
else:
    print("No")