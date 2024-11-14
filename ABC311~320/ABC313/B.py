N, M = map(int,input().split())

A = set()
B = set()

for _ in range(M):
    a,b = map(int,input().split())
    A.add(a)
    B.add(b)

result = A - B

if len(result) == 1:
    ans = result.pop()
    print(ans)
else:
    print(-1)