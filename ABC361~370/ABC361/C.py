N,K = map(int,input().split())

A = list(map(int,input().split()))

A.sort()

if N-K <= 1:
    print(0)
else:
    ans = A[N-K-1]-A[0]
    for i in range(K+1):
        cal = A[i+N-K-1]-A[i]
        if cal < ans:
            ans = cal
    print(ans)