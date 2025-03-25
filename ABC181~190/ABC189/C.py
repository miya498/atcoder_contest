N =int(input())
A = list(map(int,input().split()))

ans = 0
for left in range(N):
    x = A[left]
    for r in range(left,N):
        x = min(x,A[r])
        ans = max(ans,x*(r-left+1))

print(ans)