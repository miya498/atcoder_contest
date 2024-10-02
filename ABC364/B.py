H,W = map(int,input().split())
S = list(map(int,input().split()))
S[0] -= 1
S[1] -= 1
C = [list(input()) for _ in range(H)]
X = list(input())

for i in range(len(X)):
    h,w = S[0],S[1]
    if X[i] == "L":
        if w > 0 and C[h][w-1] == '.':
            S[1] -= 1
    elif X[i] == "R":
        if w < W-1 and C[h][w+1] == '.':
            S[1] += 1
    elif X[i] == "U":
        if h > 0 and C[h-1][w] == '.':
            S[0] -= 1
    else:
        if h != H-1  and C[h+1][w] == '.':
            S[0] += 1
print(S[0]+1,S[1]+1)