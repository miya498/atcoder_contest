from heapq import heappop, heappush
from collections import defaultdict

def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xr, yr = find(x), find(y)
        if xr == yr:
            return False
        if rank[xr] < rank[yr]:
            parent[xr] = yr
        elif rank[xr] > rank[yr]:
            parent[yr] = xr
        else:
            parent[yr] = xr
            rank[xr] += 1
        return True

    mst = []
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if union(u, v):
            mst.append((u, v, w))
    return mst

def build_tree(n, mst):
    tree = defaultdict(list)
    for u, v, w in mst:
        tree[u].append((v, w))
        tree[v].append((u, w))
    return tree

def preprocess_lca(n, tree):
    LOG = 20
    depth = [-1] * n
    parent = [[-1] * LOG for _ in range(n)]
    max_weight = [[0] * LOG for _ in range(n)]

    def dfs(v, p, d, w):
        depth[v] = d
        parent[v][0] = p
        max_weight[v][0] = w
        for u, uw in tree[v]:
            if u != p:
                dfs(u, v, d + 1, uw)

    dfs(0, -1, 0, 0)

    for k in range(1, LOG):
        for v in range(n):
            if parent[v][k - 1] != -1:
                parent[v][k] = parent[parent[v][k - 1]][k - 1]
                max_weight[v][k] = max(max_weight[v][k - 1], max_weight[parent[v][k - 1]][k - 1])

    return depth, parent, max_weight

def query_lca(x, y, depth, parent, max_weight):
    if depth[x] < depth[y]:
        x, y = y, x
    LOG = len(parent[0])
    max_w = 0
    for k in range(LOG - 1, -1, -1):
        if depth[x] - (1 << k) >= depth[y]:
            max_w = max(max_w, max_weight[x][k])
            x = parent[x][k]
    if x == y:
        return max_w
    for k in range(LOG - 1, -1, -1):
        if parent[x][k] != parent[y][k]:
            max_w = max(max_w, max_weight[x][k], max_weight[y][k])
            x = parent[x][k]
            y = parent[y][k]
    return max(max_w, max_weight[x][0], max_weight[y][0])

n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

mst = kruskal(n, edges)
tree = build_tree(n, mst)
depth, parent, max_weight = preprocess_lca(n, tree)

min_sum = float('inf')
from itertools import permutations

for perm in permutations(B):
    curr_sum = 0
    for i in range(k):
        curr_sum += query_lca(A[i] - 1, perm[i] - 1, depth, parent, max_weight)
    min_sum = min(min_sum, curr_sum)

print(min_sum)
