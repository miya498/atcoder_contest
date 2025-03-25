N,Q = map(int,input().split())

L = []

for i in range(N):
    l = list(map(int,input().split()))
    L.append(l[1:])

for i in range(Q):
    s,t = map(int,input().split())
    print(L[s-1][t-1])