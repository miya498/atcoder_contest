N,M = map(int,input().split())
S = [input() for _ in range(N)]
ans = 0

for i in range(N-1):
    for j in range(i+1,N):
        pro = ""
        for k in range(M):     
            if S[i][k] == "o" or S[j][k] == "o":
                pro += "o"
            else:
                pro += "x"
        if pro == "o"*M:
            ans += 1
print(ans)