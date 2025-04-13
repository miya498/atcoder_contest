# 入力の読み込み
N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

# 各マスに石をセットする
stones = [0] * N
for i in range(M):
    stones[X[i] - 1] = A[i]  # X[i] は 1-based なので -1 する

# 石の合計が N でなければ、目標は達成できない
if sum(stones) != N:
    print(-1)
else:
    # 操作回数のカウント
    operations = 0
    for i in range(N - 1):
        # マス i にある石の数が1個を超える場合、余剰分を右のマスへ移動
        if stones[i] > 1:
            excess = stones[i] - 1
            stones[i] = 1
            stones[i + 1] += excess
            operations += excess
    
    # すべてのマスに1つずつ石が配置されていれば結果を出力
    if all(stone == 1 for stone in stones):
        print(operations)
    else:
        print(-1)