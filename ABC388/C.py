from bisect import bisect_left

N = int(input())
A = list(map(int,input().split()))

ans = 0

for i in range(N):
    num = bisect_left(A,2*A[i],i+1)
    ans += N-num

print(ans)