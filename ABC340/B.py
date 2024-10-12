Q = int(input())

A = []

for i in range(Q):
    num,cha = list(map(int,input().split()))
    if num == 1:
        A.append(cha)
    elif num == 2:
        length = len(A)
        print(A[length-cha])