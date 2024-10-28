N,L,R = map(int,input().split())
A = list(map(int,input().split()))

ans = []
for i in range(N):
    if L < A[i] and A[i] < R:
        ans.append(A[i])
    elif A[i] <= L:
        ans.append(L)
    elif A[i] >= R:
        ans.append(R)

print(*ans)