H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

for i in range(H):
    dot = []
    for j in range(W):
        
        if A[i][j] == 0:
            dot.append(".")
        else:
            dot.append(chr(A[i][j]+64))
    print("".join(dot))
    