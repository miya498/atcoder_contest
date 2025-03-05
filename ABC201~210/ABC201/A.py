A_1,A_2,A_3 = map(int,input().split())

A = [A_1,A_2,A_3]
A.sort()

if A[2]-A[1] == A[1]-A[0]:
    print("Yes")
else:
    print("No")