N = int(input())
S = []

for i in range(N):
    cnt = 0
    s = list(input())
    for j in range(N):
        if s[j] == "o":
            cnt += 1
    S.append([cnt,i+1])

S.sort(key= lambda x: (-x[0] ,x[1]))

for i in range(N):
    print(S[i][1],end=" ")