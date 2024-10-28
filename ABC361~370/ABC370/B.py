N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]


ans = 0
for i in range(N):
    if ans < i:
        ans=A[i][ans] - 1
    else:
        ans=A[ans][i] - 1

print(ans+1)