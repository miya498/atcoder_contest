from collections import deque

def bfs(graph, start, parent):
    q = deque([start])
    parent[start] = -2  # 特別な値でスタート地点を表す

    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if parent[neighbor] == -1:  # 未訪問の頂点
                parent[neighbor] = current
                q.append(neighbor)

def find_path(N, X, Y, edges):
    # グラフを隣接リスト形式で構築
    graph = [[] for _ in range(N)]
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    # BFSで親を記録
    parent = [-1] * N
    bfs(graph, X - 1, parent)

    # 経路復元
    path = []
    current = Y - 1
    while parent[current] != -2:
        path.append(current)
        current = parent[current]
    path.append(current)

    # 経路を1-indexedで返す
    return [node + 1 for node in path[::-1]]

# 入力処理
N, X, Y = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

# 結果出力
result = find_path(N, X, Y, edges)
print(" ".join(map(str, result)))
