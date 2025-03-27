S = input()
T = input()
n_s = len(S)
n_t = len(T)
ans = 1001
for i in range(n_s-n_t+1):
    cnt = 0
    for j in range(n_t):
        if S[i+j] != T[j]:
            cnt += 1
    ans = min(ans,cnt)
print(ans)