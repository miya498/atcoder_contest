N,S,D = map(int,input().split())
X,Y = [],[]
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

ans = False
for i in range(N):
    if X[i] < S and Y[i] > D:
        ans = True
if ans:
    print("Yes")
else:
    print("No")