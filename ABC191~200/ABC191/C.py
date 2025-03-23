H,W = map(int,input().split())
S = [input() for _ in range(H)]

ang = 0
for i in range(H):
    for j in range(W):
        temp = 0
        if S[i-1][j-1] == "#":
            temp += 1
        if S[i][j-1] == "#":
            temp += 1
        if S[i-1][j] == "#":
            temp += 1
        if S[i][j] == "#":
            temp += 1
        if temp == 1 or temp == 3:
            ang += 1
print(ang)