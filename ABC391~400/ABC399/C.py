N,M = map(int,input().split())
U,V = [],[]
for _ in range(M):
    u,v = map(int,input().split())
    U.append(u)
    V.append(v)

class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
