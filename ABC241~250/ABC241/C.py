N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        cnt_b = 0
        cnt_w = 0
        if i <= N-6:
            for h in range(6):
                if S[i+h][j] == "#":
                    cnt_b += 1
                else:
                    cnt_w += 1
            if cnt_w <= 2:
                print("Yes")
                exit()

        cnt_b = 0
        cnt_w = 0
        if j <= N-6:
            for w in range(6):
                if S[i][j+w] == "#":
                    cnt_b += 1
                else:
                    cnt_w += 1
            if cnt_w <= 2:
                print("Yes")
                exit()

        cnt_b = 0
        cnt_w = 0
        if i <= N-6 and j <= N-6:
            for k in range(6):
                if S[i+k][j+k] == "#":
                    cnt_b += 1
                else:
                    cnt_w += 1
            if cnt_w <= 2:
                print("Yes")
                exit()

        cnt_b = 0
        cnt_w = 0
        if i >= 5 and j <= N-6:
            for k in range(6):
                if S[i-k][j+k] == "#":
                    cnt_b += 1
                else:
                    cnt_w += 1
            if cnt_w <= 2:
                print("Yes")
                exit()

print("No")