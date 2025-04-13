N ,M = map(int,input().split())
A = list(map(int,input().split()))

i = 0
for day in range(1,N+1):
    if day > A[i]:
        i += 1
    print(A[i]-day)

