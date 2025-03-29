N = int(input())
A = list(map(int,input().split()))
max_h = A[0]
ans = 0
for i in range(1,N):
    if A[i] < max_h:
        ans += max_h-A[i]
    else:
        max_h = A[i]
print(ans)
