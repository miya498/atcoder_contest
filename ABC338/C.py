N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

x_max = 1000000
for i in range(N):
    if A[i] != 0:
        cnt = Q[i]//A[i]
        if cnt < x_max:
            x_max = cnt

ans = 0
for x in range(0,x_max+1):
    B_list = [1000000]*N 
    for i in range(N):
        if B[i] != 0:
            y = (Q[i]-A[i]*x)//B[i]
            B_list[i] = y    
    total = x+min(B_list)
    if ans < total:
        ans = total

print(ans)