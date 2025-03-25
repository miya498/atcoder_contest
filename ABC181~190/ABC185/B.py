N,M,T = map(int,input().split())
battery = N
A,B = [0],[0]
for _ in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

for i in range(1,M+1):
    battery -= A[i] - B[i-1]
    if battery <= 0:
        print("No")
        exit()
    battery = min(N,battery+(B[i] - A[i]))

if battery-(T-B[M]) > 0:
    print("Yes")
else:
    print("No")