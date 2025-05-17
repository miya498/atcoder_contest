N = int(input())
P = list(map(int, input().split()))

# ランレングス圧縮: '<' を増加、'>' を減少の符号として長さを数える
v = []
for i in range(N - 1):
    if P[i] < P[i + 1]:
        # 増加区間
        if not v or v[-1][0] == '>':
            v.append(['<', 1])
        else:
            v[-1][1] += 1
    else:
        # 減少区間
        if not v or v[-1][0] == '<':
            v.append(['>', 1])
        else:
            v[-1][1] += 1

# +-+ パターン ('<','>','<') に対応する数を計算
ans = 0
sz = len(v)
for i in range(1, sz - 1):
    if v[i][0] == '>':
        ans += v[i - 1][1] * v[i + 1][1]

print(ans)