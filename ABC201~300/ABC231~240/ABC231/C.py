import bisect

N,Q = map(int,input().split())
A = list(map(int,input().split()))
X = [int(input()) for _ in range(Q)]

A.sort()
for x in X:
    idx = bisect.bisect_left(A,x)
    print(N-idx)
