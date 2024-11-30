N = int(input())

A = list(map(int,input().split()))
cnt = 0
for i in range(N*7):
    cnt += A[i]
    if i%7 == 6:
        print(cnt,end=" ")
        cnt = 0
