import math

N = int(input())
L = int(math.isqrt(N))  # b の最大値：b^2 <= N

ans = 0
# c は a の値の候補（a は1以上）
max_c = int(math.floor(math.log(N, 2)))
for c in range(1, max_c + 1):
    # b が属する区間： (sqrt(N/2^(c+1)), sqrt(N/2^c)] 
    b_min = int(math.floor(math.sqrt(N / (2 ** (c + 1))))) + 1
    b_max = int(math.floor(math.sqrt(N / (2 ** c))))
    # b は 1 <= b <= L である必要があるので調整
    if b_min > L:
        continue
    b_max = min(b_max, L)
    if b_min <= b_max:
        count = b_max - b_min + 1
        ans += c * count

print(ans)