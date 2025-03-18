N = int(input())
X,Y = [],[]
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        slope = (Y[j]-Y[i])/(X[j]-X[i])
        if -1 <= slope <= 1:
            ans += 1
print(ans)