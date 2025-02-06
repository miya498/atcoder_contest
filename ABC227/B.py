N = int(input())
S = list(map(int,input().split()))

cnt = 0

for s in S:
    flag = False
    for i in range(1,1000):
        for j in range(1,1000):
            if 4*i*j+3*i+3*j == s:
                cnt += 1
                flag = True
        if flag:
            break
print(N-cnt)