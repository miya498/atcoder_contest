H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(1,W):
        if S[i][j-1] == "T" and S[i][j] == "T":
            S[i][j-1] = "P"
            S[i][j] = "C"
for i in range(H):
    print("".join(S[i]))