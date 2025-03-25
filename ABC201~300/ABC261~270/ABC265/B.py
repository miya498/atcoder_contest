N,M,T = map(int,input().split())
A = list(map(int,input().split()))
X_Y = {}

for i in range(M):
    x,y = map(int,input().split())
    X_Y[x] = y

time = T
for i in range(1,N):
    if time-A[i-1] <= 0:
        print("No")
        exit()
    time -= A[i-1]
    if i+1 in X_Y:
        time += X_Y[i+1]

print("Yes")