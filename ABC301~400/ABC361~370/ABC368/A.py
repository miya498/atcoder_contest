N, K = map(int, input().split())
A = list(map(int, input().split()))

# Aの後ろからK個の要素を前に持ってくる
B_f = A[N-K:]  # 後ろからK個の要素
B_b = A[:N-K]  # 残りの要素

B = B_f + B_b  # 新しい配列を作成

# joinを使うためにmapでBの要素を文字列に変換
print(" ".join(map(str, B)))