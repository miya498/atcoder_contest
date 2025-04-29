from itertools import permutations
N = int(input())
X,Y = [],[]
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

ans = 0
for perm in permutations(range(N)):
    for i,j in zip(perm,perm[1:]):
        ans += ((X[i] - X[j])**2 + (Y[i] - Y[j])**2)**0.5

for i in range(1,N+1):
    ans /= i

print(ans)
