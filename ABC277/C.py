from collections import deque

# 入力の読み込み
N = int(input())
edges = {}

# グラフの構築
for _ in range(N):
    A, B = map(int, input().split())
    if A not in edges:
        edges[A] = []
    if B not in edges:
        edges[B] = []
    edges[A].append(B)
    edges[B].append(A)

# BFSの準備
visited = set()
queue = deque([1])  # 1階からスタート
visited.add(1)
max_floor = 1

# BFS開始
while queue:
    current = queue.popleft()
    max_floor = max(max_floor, current)
    for neighbor in edges.get(current, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

# 結果を出力
print(max_floor)