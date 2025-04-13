import math
N,M = map(int,input().split())

board = []

for i in range(M):
    s = list(map(int,input().split()))
    board.append(s)

good_set = set()

for i in range(M):
    for j in range(1,N):
        if board[i][j] < board[i][j-1]:
            good_set.add((board[i][j],board[i][j-1]))
        else:
            good_set.add((board[i][j-1],board[i][j]))

ans = math.comb(N,2) - len(good_set)

print(ans)