H,W = map(int,input().split())
S = [input() for _ in range(H)]

flag = True
x_1 = -1
y_1 = -1
min_i = 100000
min_j = 100000
max_i = -1
max_j = -1
for i in range(H):
    for j in range(W):
        if flag and S[i][j] == "#":
            x_1 = i
            y_1 = j
            max_i = max(max_i,i)
            max_j = max(max_j,j)
            min_i = min(min_i,i)
            min_j = min(min_j,j)
            flag = False
        elif S[i][j] == "#":
            max_i = max(max_i,i)
            max_j = max(max_j,j)
            min_i = min(min_i,i)
            min_j = min(min_j,j)

for i in range(min_i,max_i+1):
    for j in range(min_j,max_j+1):
        if S[i][j] == ".":
            print("No")
            exit()

print("Yes")




