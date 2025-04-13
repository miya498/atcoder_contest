a,b,c = map(int,input().split())
A = [a,b,c]
A.sort()
if A[0]*A[1]==A[2]:
    print("Yes")
else:
    print("No")