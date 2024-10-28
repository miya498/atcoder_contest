A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

ab = pow(A[0]-B[0],2)+pow(A[1]-B[1],2)
bc = pow(C[0]-B[0],2)+pow(C[1]-B[1],2)
ca = pow(A[0]-C[0],2)+pow(A[1]-C[1],2)

if ab > bc and ab > ca:
    if ab==bc+ca:
        print("Yes")
    else:
        print("No")
elif bc > ab and bc > ca:
    if bc==ab+ca:
        print("Yes")
    else:
        print("No")
else:
    if ca==bc+ab:
        print("Yes")
    else:
        print("No")