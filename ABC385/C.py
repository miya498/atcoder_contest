N = int(input())
H = list(map(int, input().split()))

ans = 1  # 最低でも1つのビルを選べる

for k in range(1, N):  # 間隔 k を全探索
    for i in range(k):  # 開始位置 i を全探索
        current_height = None  # 現在の高さを追跡
        count = 0  # 現在の連続カウント
        for j in range(i, N, k):  # 等間隔で進む
            if current_height != H[j]:  # 高さが異なる場合
                current_height = H[j]  # 高さを更新
                count = 1  # リセットして再カウント
            else:
                count += 1  # 連続するビルをカウント
            ans = max(ans, count)  # 最大値を更新

print(ans)