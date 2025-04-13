N,M = map(int,input().split())

A = list(map(int,input().split()))

A.sort()
A.append(9000000001)

ans = 0
r = 0
for l in range(0,N):
    while A[r] < A[l]+M:
        r += 1
    ans = max(ans,r-l)
print(ans)