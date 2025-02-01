N = int(input())
A = list(map(int,input().split()))

for i in range(1,N-1):
    if A[i]**2 != A[i-1]*A[i+1]:
        print("No")
        exit()
print("Yes")