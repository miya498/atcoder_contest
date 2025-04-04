import bisect

N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_t = [0]*(N+1)
B_t = [0]*(M+1)
for i in range(1,N+1):
    A_t[i] += A_t[i-1] + A[i-1]
for i in range(1,M+1):
    B_t[i] += B_t[i-1] + B[i-1]
ans = 0
for i in range(N+1):
    time = K-A_t[i]
    if time < 0:
        break
    j = bisect.bisect_right(B_t,time)
    ans = max(ans,i+j-1)
print(ans)

