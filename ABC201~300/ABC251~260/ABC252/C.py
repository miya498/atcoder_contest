N = int(input())
S = [input() for _ in range(N)]

time = [[] for _ in range(10)]

Count = [[0]*10 for _ in range(10)]

for i in range(N):
    for j in range(10):
        S_int = int(S[i][j])
        Count[S_int][j] += 1
        time[S_int].append(j+(Count[S_int][j]-1)*10)

ans = 10**9

for i in range(10):
    ans = min(ans,max(time[i]))

print(ans)     
        

        