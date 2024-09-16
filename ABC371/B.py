N,M = map(int, input().split())

home = ["T" for _ in range(N)]

A = list()
B = list()
for i in range(M):
    a,b = input().split()
    A.append(int(a))
    B.append(b)

for i in range(M):
    a = A[i]
    b = B[i]
    if(home[a-1]=="T" and b=="M"):
        print("Yes")
        home[a-1]="F"
    else:
        print("No")
