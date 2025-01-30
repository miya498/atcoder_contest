import math
N = int(input())
X,Y = [],[]

for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
ans = -1

for i in range(N-1):
    for j in range(i+1,N):
        dis = math.sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2)
        if ans < dis:
            ans = dis
print(ans)