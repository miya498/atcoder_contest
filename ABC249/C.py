from collections import Counter

# 入力
N, K = map(int, input().split())
S = [input() for _ in range(N)]

# 結果の最大値
max_count = 0

# bit全探索 (0〜2^N-1)
for bit in range(1 << N):
    # 選ばれた文字列に含まれる文字をカウント
    char_count = Counter()
    for i in range(N):
        if (bit >> i) & 1:  # i 番目の文字列を選ぶ場合
            char_count.update(S[i])
    
    # ちょうど K 回現れる文字の種類数を計算
    current_count = sum(1 for v in char_count.values() if v == K)
    
    # 最大値を更新
    max_count = max(max_count, current_count)

# 出力
print(max_count)