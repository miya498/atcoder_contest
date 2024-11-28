N,T = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))

flag = False
for i in range(N):
    if C[i] == T:
        flag = True
        break

if flag:
    ans = 0
    idx = -1
    for i in range(N):
        if C[i] == T:
            if ans < R[i]:
                ans = R[i]
                idx = i+1
    print(idx)
else:
    T = C[0]
    ans = 0
    idx = -1
    for i in range(N):
        if C[i] == T:
            if ans < R[i]:
                ans = R[i]
                idx = i+1
    print(idx)

