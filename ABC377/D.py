# 入力の受け取り
N, M = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

# 全ての (l, r) 組み合わせを作成
all_pairs = set((l, r) for l in range(1, M + 1) for r in range(l, M + 1))

# 含んでしまう (l, r) の組み合わせを保持する
excluded_pairs = set()

# 各区間 [Li, Ri] について、完全に含む (l, r) を excluded_pairs に追加
for L, R in intervals:
    for l in range(1, L + 1):
        for r in range(R, M + 1):
            excluded_pairs.add((l, r))

# 条件を満たす (l, r) の組み合わせ数を計算
valid_pairs = all_pairs - excluded_pairs
print(len(valid_pairs))
