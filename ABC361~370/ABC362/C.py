N = int(input())
L = []
R = []
for i in range(N):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)

if sum(L) > 0 or sum(R) < 0:
    print("No")
    exit()

X = L.copy()
sumX = sum(X)
for i in range(N):
    d = min(R[i]-L[i],-sumX)
    sumX += d
    X[i] += d 

print("Yes")
print(*X)