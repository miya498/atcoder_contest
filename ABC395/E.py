import heapq

# 入力の受け取り
n, m, x = map(int, input().split())

# グラフの作成 (通常のグラフと反転グラフ)
graph = [[] for _ in range(n+1)]      # 通常の辺
rev_graph = [[] for _ in range(n+1)]  # 反転した辺

# 辺の入力
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)       # 通常の方向
    rev_graph[v].append(u)   # 逆向きの辺を追加

# 距離リスト (dist[i][0]: 通常の向き, dist[i][1]: 逆向きで移動可能)
dist = [[float('inf')] * 2 for _ in range(n+1)]
dist[1][0] = 0  # 開始地点のコストを 0 にする (通常向き)

# 優先度付きキュー (コスト, 現在の頂点, 現在の状態) -> ダイクストラ法
queue = [(0, 1, 0)]  # (コスト, 頂点, 状態)

# ダイクストラ法による最短経路探索
while queue:
    cost, v, state = heapq.heappop(queue)

    # 既に最適なコストよりも大きければスキップ
    if cost > dist[v][state]:
        continue

    # 現在の状態に応じたグラフを選択 (state=0: 通常, state=1: 反転)
    curr_graph = graph if state == 0 else rev_graph

    # 隣接する頂点への更新
    for next_v in curr_graph[v]:
        if dist[next_v][state] > cost + 1:
            dist[next_v][state] = cost + 1
            heapq.heappush(queue, (cost + 1, next_v, state))

    # 状態を反転 (通常 <-> 逆向き) して移動可能な場合を考慮
    next_state = 1 - state
    if dist[v][next_state] > cost + x:
        dist[v][next_state] = cost + x
        heapq.heappush(queue, (cost + x, v, next_state))

# 頂点 n への最短距離を取得 (通常向き or 逆向きの最小値)
result = min(dist[n][0], dist[n][1])
print(result)
