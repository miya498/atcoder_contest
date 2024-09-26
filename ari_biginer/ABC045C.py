S = input()

N = len(S)
ans = 0

for bit in range(2 ** (N - 1)):
    s = S[0]
    total = 0

    for i in range(N - 1):

        if bit & (1 << i):
            total += int(s)
            s = ""
        s += S[i + 1]    
    total += int(s)
    # 合計を更新
    ans += total

print(ans)