N,M = map(int,input().split())
A,B = [],[]
for _ in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
K = int(input())
C,D = [],[]
for _ in range(K):
    c,d = map(int,input().split())
    C.append(c)
    D.append(d)

ans = 0
for mask in range(1<<K):
    plates = [0]*(N+1)
    for i in range(K):
        if mask & (1<<i):
            plates[D[i]] = 1
        else:
            plates[C[i]] = 1
    cnt = 0
    for i in range(M):
        if plates[A[i]] and plates[B[i]]:
            cnt += 1
    ans = max(ans,cnt)
print(ans)