from collections import deque

# 入力の読み込み
N, D = map(int, input().split())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

# BFS 用のキューと訪問済みフラグ
infected = [False] * N
queue = deque([0])  # 人1（index 0）から開始
infected[0] = True

# BFS の実行
while queue:
    current = queue.popleft()
    x1, y1 = coordinates[current]
    for i in range(N):
        if not infected[i]:  # 未感染なら計算する
            x2, y2 = coordinates[i]
            # ユークリッド距離の計算
            distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
            if distance_squared <= D ** 2:
                infected[i] = True
                queue.append(i)

# 結果の出力
for is_infected in infected:
    print("Yes" if is_infected else "No")