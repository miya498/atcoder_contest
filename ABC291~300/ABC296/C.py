N,X = map(int,input().split())
A = list(map(int,input().split()))
A_set = set(A)

for i in range(N):
    if A[i]+X in A_set:
        print("Yes")
        exit()   

print("No")