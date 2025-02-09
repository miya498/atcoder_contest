N,M = map(int,input().split())
A = list(map(int,input().split()))

if N == M:
    print(0)
    exit()

ans = [i for i in range(1,N+1)]

for i in range(M):
    ans.remove(A[i])

print(N-M)
print(*ans)