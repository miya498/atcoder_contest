N,M = map(int,input().split())

S =[]

for i in range(N):
    s = list(input())
    S.append(s)

for i in range(N):
    for j in range(M):
        flag = True

        for x in range(i,i+3):
            for y in range(j,j+3):
                if not (0 <= x <= N-1 and 0 <= y <= M-1 and S[x][y] == "#"):
                    flag = False
        
        for x in range(i+6,i+9):
            for y in range(j+6,j+9):
                if not (0 <= x <= N-1 and 0 <= y <= M-1 and S[x][y] == "#"):
                    flag = False
        
        for x in range(i,i+4):
            y = j + 3
            if not (0 <= x <= N-1 and 0 <= y <= M-1 and S[x][y] == "."):
                    flag = False

        for y in range(j,j+4):
            x = i + 3
            if not (0 <= x <= N-1 and 0 <= y <= M-1 and S[x][y] == "."):
                    flag = False

        for x in range(i+5,i+9):
            y = j + 5
            if not (0 <= x <= N-1 and 0 <= y <= M-1 and S[x][y] == "."):
                    flag = False

        for y in range(j+5,j+9):
            x = i + 5
            if not (0 <= x <= N-1 and 0 <= y <= M-1 and S[x][y] == "."):
                    flag = False

        if flag:
            print(i+1,j+1)

        

