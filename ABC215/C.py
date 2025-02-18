from itertools import permutations

S, K = input().split()
K = int(K)

# すべての順列を生成して辞書順にソート
ans = sorted(set("".join(p) for p in permutations(S)))

# K番目の順列（0-index なので K-1）
print(ans[K-1])