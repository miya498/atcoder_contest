N,S,K = map(int,input().split())

ans = 0

for _ in range(N):
    p,q = map(int,input().split())
    ans += p*q

if ans < S:
    print(ans+K)
else:
    print(ans)