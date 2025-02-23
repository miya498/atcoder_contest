import bisect
H,W,N = map(int,input().split())
A,B = [],[]

for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

X = list(set(A))
X.sort()
Y = list(set(B))
Y.sort()

for i in range(N):
    x = bisect.bisect_left(X,A[i])+1
    y = bisect.bisect_left(Y,B[i])+1
    print(x,y)