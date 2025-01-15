N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

max_value = max(A)

for i in range(K):
    if A[B[i]-1] == max_value:
        print("Yes")
        exit()
print("No")