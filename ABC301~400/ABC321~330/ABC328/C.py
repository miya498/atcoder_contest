N,Q = map(int,input().split())
S =input()
S_ruiseki = [0]*N
cnt = 0
for i in range(1,N):
    if S[i] == S[i-1]:
        cnt += 1
    S_ruiseki[i] = cnt

for i in range(Q):
    l,r = map(int,input().split())
    ans = S_ruiseki[r-1] - S_ruiseki[l-1]
    print(ans)