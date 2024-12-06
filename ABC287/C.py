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
            return True
        return False

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Union-Find 初期化
uf = UnionFind(N)

# 各頂点の次数を数える配列
degree = [0] * N

# 辺を処理
for u, v in edges:
    u -= 1
    v -= 1
    if not uf.union(u, v):  # 閉路がある場合
        print("No")
        exit()
    degree[u] += 1
    degree[v] += 1

# 条件1: 連結成分が1つであること
if len(set(uf.find(i) for i in range(N))) > 1:
    print("No")
    exit()

# 条件2: 辺の数が N-1 であること
if M != N - 1:
    print("No")
    exit()

# 条件3: 各頂点の次数が2以下であること
if any(d > 2 for d in degree):
    print("No")
    exit()

# すべての条件を満たす
print("Yes")
