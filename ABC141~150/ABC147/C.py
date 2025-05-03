N = int(input())
word = []

for i in range(N):
    a = int(input())
    X = []
    for j in range(a):
        x,y = map(int,input().split())
        X.append([x,y])
    word.append(X)

ans = 0
for i in range(2**N):
    mask = []
    for j in range(N):
        if (i >> j) & 1:
            mask.append(1)
        else:
            mask.append(0)
    flag = True
    for j in range(N):
        if (i >> j) & 1:
            for k in range(len(word[j])):
                if word[j][k][1] == 1:
                    if mask[word[j][k][0]-1] == 1:
                        continue
                    else:
                        flag = False
                        break
                else:
                    if mask[word[j][k][0]-1] == 0:
                        continue
                    else:
                        flag = False
                        break
    if flag:
        ans = max(ans,bin(i).count("1"))

print(ans)
