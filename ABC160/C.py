K,N = map(int,input().split())
A = list(map(int,input().split()))

ans = 1000000000
for i in range(N):
    if i == 0:
        distance = min(K-(A[i+1]-A[i]),A[N-1]-A[i])
    elif i == N-1:
        distance = min(K-(A[i]-A[i-1]),A[i]-A[0])
    else:
        distance = min(K-(A[i]-A[i-1]),K-(A[i+1]-A[i]))
    ans = min(ans,distance)

print(ans)
