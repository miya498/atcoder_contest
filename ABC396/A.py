N = int(input())
A = list(map(int,input().split()))

ans = False

for i in range(N-2):
    if A[i] == A[i+1] == A[i+2]:
        print("Yes")
        exit()
print("No")