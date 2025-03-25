N,M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans_1 = []
ans_2 = []
i,j,cnt = 0,0,0
while i < N or j < M:

    if i == N:
        cnt += 1
        ans_2.append(cnt)
        j += 1
    elif j == M:
        cnt += 1
        ans_1.append(cnt)
        i += 1
    elif A[i] < B[j]:
        cnt += 1
        ans_1.append(cnt)
        i += 1
    else:
        cnt += 1
        ans_2.append(cnt)
        j += 1
print(*ans_1)
print(*ans_2) 
