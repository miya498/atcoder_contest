N = int(input())
X,Y = [],[]
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if (Y[j]-Y[i])*(X[k]-X[j]) == (Y[k]-Y[j])*(X[j]-X[i]):
                print("Yes")
                exit()
print("No")