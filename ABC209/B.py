N,X = map(int,input().split())
A = list(map(int,input().split()))

total = 0
for i in range(N):
    if (i+1) % 2 == 0:
        total += A[i]-1
    else:
        total += A[i]
if X >= total:
    print("Yes")
else:
    print("No")