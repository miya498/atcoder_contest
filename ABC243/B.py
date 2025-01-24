N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt_1 = 0
for i in range(N):
    if A[i] == B[i]:
        cnt_1 += 1

cnt_2 = 0
for i in range(N):
    for j in range(N):
        if A[i] == B[j] and i != j:
            cnt_2 += 1
print(cnt_1)
print(cnt_2)