def judge(a,b):
    if (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        return 1
    elif (a == "P" and b == "C") or (a == "G" and b == "P") or (a == "C" and b == "G"):
        return -1
    else:
        return 0

N,M = map(int,input().split())
A = [input() for _ in range(2*N)]
ans = [[0,i+1] for i in range(2*N)]

for j in range(M):
    ans.sort(key=lambda x: (-x[0],x[1]))
    for i in range(N):
        idx_1 = ans[2*i][1]-1
        idx_2 = ans[2*i+1][1]-1
        if judge(A[idx_1][j],A[idx_2][j]) == 1:
            ans[2*i][0] += 1
        elif judge(A[idx_1][j],A[idx_2][j]) == -1:
            ans[2*i+1][0] += 1

ans.sort(key=lambda x: (-x[0],x[1]))
for _,a in ans:
    print(a)