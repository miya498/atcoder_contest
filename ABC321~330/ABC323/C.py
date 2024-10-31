N, M = map(int, input().split())
A = list(map(int, input().split()))

# A の得点リストを降順にソート（スコアが高い順）
A_list = sorted([(i, A[i]) for i in range(M)], key=lambda x: -x[1])

S = []             # 各参加者の回答
score_table = []   # 各参加者のスコア
saikou = 0         # 最高スコア

# 各参加者のスコア計算
for i in range(N):
    score = 0
    s = list(input())
    for j in range(M):
        if s[j] == "o":
            score += A[j]
    saikou = max(saikou, score+i+1)
    S.append(s)
    score_table.append(score+i+1)

# 各参加者のスコアを比較して、最高スコアとの差を埋めるための最小操作数を求める
for i in range(N):
    current_score = score_table[i]
    cnt = 0

    # 最高スコアに到達している場合は 0 を出力
    if current_score == saikou:
        print(0)
        continue

    # スコアを追加して、最高スコアに到達するまでの回数をカウント
    for j in range(M):
        if S[i][A_list[j][0]] == "x":  # 未回答の問題のみ追加
            current_score += A_list[j][1]
            cnt += 1
            if current_score >= saikou:
                print(cnt)
                break