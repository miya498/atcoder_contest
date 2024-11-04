N = int(input())

zahyou = [["."]*100 for _ in range(100)]

for _ in range(N):
    a,b,c,d = map(int,input().split())
    for i in range(a,b):
        for j in range(c,d):
            zahyou[i][j] = "#"

cnt = 0

for i in range(100):
    for j in range(100):
        if zahyou[i][j] == "#":
            cnt += 1

print(cnt)