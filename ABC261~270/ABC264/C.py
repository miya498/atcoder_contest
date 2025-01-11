H_1,W_1 = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H_1)]

H_2,W_2 = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(H_2)]

def get_matrix(matrix,h,w):
    return [[matrix[H][W] for W in w] for H in h ]
for h_mask in range(1<<H_1):
    for w_mask in range(1<<W_1):
        h = [i for i in range(H_1) if (h_mask&(1<<i))]
        w = [j for j in range(W_1) if (w_mask&(1<<j))]

        if len(h) != H_2 or len(w) != W_2:
            continue

        submatrix = get_matrix(A,h,w)

        if submatrix == B:
            print("Yes")
            exit()
print("No")