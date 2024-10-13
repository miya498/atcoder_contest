N = int(input())
S = list(input())

cnt = 0
for i in range(N - 2):
    if S[i] == '#' and S[i+1] == '.' and S[i+2] == '#':
        cnt += 1

print(cnt)
