H,W = map(int,input().split())

S = []

for i in range(H):
    s = list(input())
    S.append(s)

min_i,max_i = 1000,-1
min_j,max_j = 1000,-1

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            min_i = min(min_i,i)
            max_i = max(max_i,i)
            min_j = min(min_j,j)
            max_j = max(max_j,j)
for i in range(min_i,max_i+1):
    for j in range(min_j,max_j+1):
        if S[i][j] == ".":
            print(i+1,j+1)            