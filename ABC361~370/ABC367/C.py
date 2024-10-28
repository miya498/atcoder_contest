def find_sequences(N, R, K):
    # 結果を保存するリスト
    results = []

    # 再帰的にすべての列を生成して条件を満たすものを収集する関数
    def dfs(seq, total):
        # 長さがNになったらチェック
        if len(seq) == N:
            if total % K == 0:  # 総和がKの倍数であるか
                results.append(seq[:])  # 結果リストに追加
            return
        
        # 次の数を1からRiまで順番に探索
        next_index = len(seq)
        for i in range(1, R[next_index] + 1):
            dfs(seq + [i], total + i)

    # 初期化して探索開始
    dfs([], 0)

    # 辞書順に結果を出力
    for res in results:
        print(" ".join(map(str, res)))


# 入力の受け取り
N, K = map(int, input().split())  # NとKの入力
R = list(map(int, input().split()))  # 各要素の上限値Riの入力

# 関数呼び出し
find_sequences(N, R, K)