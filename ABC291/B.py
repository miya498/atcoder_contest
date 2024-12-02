N = int(input())
X = list(map(int,input().split()))
sum_score = sum(X)
X.sort()
for i in range(N):
    sum_score -= X[i]

X.sort(reverse=True)
for i in range(N):
    sum_score -= X[i]

ans = sum_score/(3*N)
print(ans)
