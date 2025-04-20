# N: 食材の種類数（1〜N）
# M: 料理の数（1〜M）
N, M = map(int, input().split())

# dishes[i] は i 番目の料理に使われている食材のリスト（0-indexed）
dishes = [[] for _ in range(M)]

# used[x] は 食材 x（1-indexed）が使われている料理のインデックス一覧
used = [[] for _ in range(N+1)]

# 料理の入力処理
for i in range(M):
    data = list(map(int, input().split()))
    X = data[0]        # 食材の数
    A = data[1:]       # 食材リスト
    dishes[i] = A
    for a in A:
        used[a].append(i)  # 食材 a が使われている料理 i を登録

# B[i]: i 日目に克服する食材の番号（長さ N）
B = list(map(int, input().split()))

# 各料理について、まだ克服していない（苦手な）食材の数を管理
NG_cnt = [0] * M

# 最初はすべての食材を克服済みなので、全料理が食べられる
eat = M

# 出力結果（各日で食べられる料理の数）を保存する
res = [0] * N

# 食材を逆順（N日目 → 1日目）にして処理
for day in range(N-1, -1, -1):
    res[day] = eat  # 現時点で食べられる料理の数を保存

    bad = B[day]    # その日に苦手に「戻す」食材

    # その食材が使われているすべての料理をチェック
    for dish in used[bad]:
        if NG_cnt[dish] == 0:
            # 今までこの料理は食べられていたが、
            # この食材を苦手に戻すことで食べられなくなる
            eat -= 1
        NG_cnt[dish] += 1  # 料理 dish に含まれる苦手食材の数を1つ増やす

# 各日（1〜N日目）に食べられる料理の数を順に出力
for i in range(N):
    print(res[i])