N = int(input())
X,Y = [],[]
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (X[i]-X[k])*(Y[i]-Y[j]) != (Y[i]-Y[k])*(X[i]-X[j]):
                ans += 1
print(ans)
