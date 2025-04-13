N,M = map(int,input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for a in range(N-M+1):
    for b in range(N-M+1):
        ans = True
        for i in range(M):
            for j in range(M):
                if S[a+i][b+j] != T[i][j]:
                    ans = False
                    break
            if not ans:
                break

        if ans:
            print(a+1,b+1)
            exit()