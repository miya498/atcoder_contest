N,P,Q = map(int,input().split())

D = list(map(int,input().split()))

ans = P

for i in range(N):
    if ans > Q+D[i]:
        ans = Q+D[i]

print(ans)