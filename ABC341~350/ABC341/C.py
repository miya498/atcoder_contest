H,W,N = map(int,input().split())
T = list(input())
S = []
for i in range(H):
    s = list(input())
    S.append(s)
ans = 0

for h in range(H):
    for w in range(W):
        x,y = h,w
        if S[x][y] == ".":
            for i in range(N):
                if T[i] == 'L':
                    if S[x][y-1] == "#":
                        break
                    else:
                        y = y-1

                elif T[i] == 'R':
                    if S[x][y+1] == "#":
                        break
                    else:
                        y = y+1

                elif T[i] == 'U':
                    if S[x-1][y] == "#":
                        break
                    else:
                        x = x-1
                elif T[i] == 'D':
                    if S[x+1][y] == "#":
                        break
                    else:
                        x = x+1
                
                if i == N-1:
                    ans += 1

print(ans)