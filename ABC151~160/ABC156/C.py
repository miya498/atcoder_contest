N = int(input())
X = list(map(int,input().split()))
ans = 10**9
for i in range(101):
    rally = 0
    for j in range(N):
        rally += (X[j] - i) ** 2
    ans = min(ans,rally)

print(ans)
