class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1


# 入力の受け取り
N, M = map(int, input().split())
a = list(map(int, input().split()))

# Union-Findの初期化
uf = UnionFind(N)

# 辺を追加
for ai in a:
    uf.union(ai - 1, ai)

# 各連結成分の要素をグループ化
groups = {}
for i in range(N):
    root = uf.find(i)
    if root not in groups:
        groups[root] = []
    groups[root].append(i + 1)

# 辞書順に各グループを降順でソートして結果を生成
result = []
for group in sorted(groups.values(), key=lambda x: min(x)):
    result.extend(sorted(group, reverse=True))

# 結果の出力
print(*result)
