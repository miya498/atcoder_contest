N,D = map(int,input().split())

S = []
for i in range(N):
    s = list(input())
    S.append(s)

ans = 0
cnt = 0

for i in range(D):
    flag = True
    for j in range(N):
        if S[j][i] == "x":
            flag = False
            break
    
    if flag:
        cnt += 1
    else:
        cnt = 0

    ans = max(cnt,ans) 

print(ans)
