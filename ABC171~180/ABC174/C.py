K = int(input())
num = 0
for i in range(K):
    num = (num*10+7)%K
    if num == 0:
        print(i+1)
        exit()
print(-1)