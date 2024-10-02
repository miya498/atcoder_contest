N,X,Y = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

tep = 0
A_min = 0
for i in range(N):
    tep += A[i]
    A_min += 1
    if tep > X:
        break
tep = 0
B_min = 0
for i in range(N):
    tep += B[i]
    B_min += 1
    if tep > Y:  
        break

if A_min <= B_min:
    print(A_min)
else:
    print(B_min)