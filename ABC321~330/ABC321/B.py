N,X = map(int,input().split())
A = list(map(int,input().split()))

A.sort()
flag =True
i = 0
for i in range(max(A)+2):
    B = A.copy()
    B.append(i)
    keisan = sum(B)-min(B)-max(B)
    if keisan >= X:
        ans = i
        flag = False
        print(ans)
        break

if flag:
    print(-1)