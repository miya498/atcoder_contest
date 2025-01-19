N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 1. 数学の点数が高い方から X 人を合格
math_scores = [(A[i], i + 1) for i in range(N)]  # (点数, 受験番号)
math_scores.sort(key=lambda x: (-x[0], x[1]))  # 点数の降順、受験番号の昇順
passed = set()
for i in range(X):
    passed.add(math_scores[i][1])

# 2. 英語の点数が高い方から Y 人を合格
english_scores = [(B[i], i + 1) for i in range(N) if (i + 1) not in passed]
english_scores.sort(key=lambda x: (-x[0], x[1]))
for i in range(Y):
    passed.add(english_scores[i][1])

# 3. 数学と英語の合計点が高い方から Z 人を合格
total_scores = [(A[i] + B[i], i + 1) for i in range(N) if (i + 1) not in passed]
total_scores.sort(key=lambda x: (-x[0], x[1]))
for i in range(Z):
    passed.add(total_scores[i][1])

# 合格者の番号を小さい順に出力
for number in sorted(passed):
    print(number)