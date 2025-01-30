from collections import Counter
from collections import defaultdict
N,Q = map(int,input().split())
A = list(map(int,input().split()))
a = Counter(A)
d = defaultdict(list)


for i in range(N):
    d[A[i]].append(i+1)

for _ in range(Q):
    x,k = map(int,input().split())
    if a[x] < k:
        print(-1)
    else:
        print(d[x][k-1])