A,B = map(int,input().split())
A = list(str(A))
B = list(str(B))
n =min(len(A),len(B))

for i in range(1,n+1):
    if int(A[-i])+int(B[-i]) >=10:
        print("Hard")
        exit()

print("Easy")

