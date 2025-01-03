N = int(input())
A = list(map(int,input().split()))

ans = 0
same = 0
for i in range(N):
    A[i] -= 1
    if A[i] == i:
        same += 1

ans += same*(same-1)//2

for i,j in enumerate(A):
    if i<j and A[j] == i:
        ans += 1
    
print(ans)