N,K,M = map(int,input().split())
A = list(map(int,input().split()))
ans = N*M - sum(A)

if ans > K:
    print(-1)
elif ans <= 0:
    print(0)
else:
    print(ans)

