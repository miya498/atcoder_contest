X,N = map(int,input().split())
P = list(map(int,input().split()))
ans = -1
result = 10000
for i in range(0,102):
    if i not in P and result > abs(X-i):
        ans = i
        result = abs(X-i)
print(ans)