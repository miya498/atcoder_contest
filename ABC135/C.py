N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0

for i in range(N):

    kill = min(A[i],B[i])
    ans += kill
    A[i] -= kill
    B[i] -= kill

    kill = min(A[i+1],B[i])
    ans += kill
    A[i+1] -= kill
print(ans)