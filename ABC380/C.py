N,K = map(int,input().split())
S = input()

chunks = []
i = 0

while i < N:
    if S[i] == '1':
        start = i
        while i < N and S[i] == '1':
            i += 1
        chunks.append((start, i - 1))  # (始まり, 終わり)
    else:
        i += 1

# K番目の塊を移動
kth_start, kth_end = chunks[K - 1]  # K番目の1の塊の範囲
prev_end = chunks[K - 2][1]         # K-1番目の塊の終了位置

# 新しい配列で構築
result = list(S)
# 1 の塊を移動
for i in range(kth_start, kth_end + 1):
    result[i] = '0'
for i in range(prev_end + 1, prev_end + 1 + (kth_end - kth_start + 1)):
    result[i] = '1'

print(''.join(result))
