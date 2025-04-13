N,M = map(int,input().split())
S = []
for i in range(N):
    s = input()
    S.append(s)

ans = N 

for bit in range(2 ** N):   
    cnt = 0
    exist = [False]*M
    for i in range(N):
        if bit & (1 << i):
            cnt += 1
            for j in range(M):
                if S[i][j] == 'o':
                    exist[j] = True
    if all(exist):
        ans = min(ans,cnt)    

print(ans)