N = int(input())
S = []

# 棒の文字列を入力として取得
for i in range(N):
    s = input()
    S.append(s)

# 棒の種類を集合で管理
S_set = set()

# 各棒の文字列とその逆順を集合に追加
for i in range(N):
    sakasa = S[i][::-1]
    # 文字列またはその逆順が集合にない場合のみ追加
    if S[i] not in S_set and sakasa not in S_set:
        S_set.add(S[i])

# 集合の要素数が異なる種類の棒の数
print(len(S_set))