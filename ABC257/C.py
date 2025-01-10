N = int(input())
S = input()
W = list(map(int, input().split()))

# 体重の情報を (体重, 本来の属性) のペアにしてリスト化
people = [(W[i], int(S[i])) for i in range(N)]

# 体重でソート
people.sort()

# 初期値として、すべての人を子供と判定した場合の正答数
correct = sum(1 for _, attr in people if attr == 0)
max_correct = correct

# 境界値ごとに正答数を計算
for i in range(N):
    if people[i][1] == 0:
        correct -= 1  # 本来の子供を大人と判定する
    else:
        correct += 1  # 本来の大人を大人と判定する

    # 次の体重が同じならスキップ
    if i < N - 1 and people[i][0] == people[i + 1][0]:
        continue

    # 正答数を更新
    max_correct = max(max_correct, correct)

# 結果を出力
print(max_correct)