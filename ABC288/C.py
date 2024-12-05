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

uf = UnionFind(N)
redundant_edges = 0

for a, b in edges:
    a -= 1
    b -= 1
    if not uf.union(a, b):
        redundant_edges += 1

print(redundant_edges)
