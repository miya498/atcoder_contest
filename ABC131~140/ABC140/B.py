N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = 0
eat = -1
for i in range(N):
    if not eat == -1:
        if A[i] == eat+1:
            ans += B[A[i]-1]
            ans += C[eat-1]
            eat = A[i]
        else:
            ans += B[A[i]-1]
            eat = A[i]
    else:
        ans += B[A[i]-1]
        eat = A[i]
print(ans)
