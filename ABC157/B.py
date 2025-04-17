A = [list(map(int,input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]
bingo = [[False]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        if A[i][j] in B:
            bingo[i][j] = True

for i in range(3):
    if bingo[i][0] and bingo[i][1] and bingo[i][2]:
        print("Yes")
        exit()
    if bingo[0][i] and bingo[1][i] and bingo[2][i]:
        print("Yes")
        exit() 

if bingo[0][0] and bingo[1][1] and bingo[2][2]:
    print("Yes")
    exit()
if bingo[0][2] and bingo[1][1] and bingo[2][0]:
    print("Yes")
    exit()

print("No")
