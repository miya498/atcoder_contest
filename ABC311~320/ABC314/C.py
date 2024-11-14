N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

# 各色のインデックスを格納するリスト
P = [[] for _ in range(M)]
for i in range(N):
    P[C[i] - 1].append(i)

# 出力用のリストを初期化
ans = [''] * N

# 各色のインデックスを回転させて並べ替えを行う
for i in range(M):
    if len(P[i]) > 1:
        # 回転処理：最後のインデックスを最初に移動
        P[i] = [P[i][-1]] + P[i][:-1]
    # ans に対応する文字をセット
    for j in range(len(P[i])):
        ans[P[i][j]] = S[P[i][(j - 1) % len(P[i])]]

# 結果を結合して出力
print("".join(ans))