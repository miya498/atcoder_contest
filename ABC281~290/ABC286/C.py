N,A,B = map(int,input().split())
S = input()

ans = 5001000000000

for i in range(N):
    cnt = 0
    for j in range(N//2):
        if S[j] != S[N-j-1]:
            cnt += B
    
    ans = min(ans,cnt+A*i)
    S = S[1:]+S[0]

print(ans)
