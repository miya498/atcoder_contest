N = int(input())
A = []

for i in range(N):
    c = int(input())
    a = list(map(int,input().split()))
    A.append(a)

X = int(input())

ans = []
for i in range(N):
    for j in range(len(A[i])):
        if A[i][j] == X:
            ans.append(i)

if len(ans) == 0:
    print(0)
else:
    saisyou = 37
    kotae = []
    for i in range(len(ans)):
        saisyou = min(saisyou,len(A[ans[i]]))

    for i in range(len(ans)):
        if saisyou == len(A[ans[i]]):
            kotae.append(ans[i]+1)

    kotae.sort
    print(len(kotae))
    print(*kotae)