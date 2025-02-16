from collections import defaultdict

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

remove_count = 0
edge_count = defaultdict(int)

for u, v in edges:
    if u == v:
        remove_count += 1
    else:
        edge_count[(min(u, v), max(u, v))] += 1

for count in edge_count.values():
    if count > 1:
        remove_count += count - 1

print(remove_count)
