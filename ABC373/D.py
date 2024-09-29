from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, -w))  # 無向グラフに変換するために逆方向も追加

# 頂点の値を保持する配列、すべての頂点の初期値を None（未確定）とする
values = [None] * (N + 1)

# すべての連結成分を探索するためのループ
for start in range(1, N + 1):
    if values[start] is None:  # 未確定の頂点から開始
        values[start] = 0  # 任意の開始点の値を0にする
        queue = deque([start])

        # BFS で各頂点の値を確定させていく
        while queue:
            u = queue.popleft()

            # u の隣接する頂点 v の値を更新
            for v, w in graph[u]:
                if values[v] is None:  # vの値がまだ決まっていない場合
                    values[v] = values[u] + w
                    queue.append(v)


output = [str(values[i])  for i in range(1, N + 1)]
print(" ".join(output))