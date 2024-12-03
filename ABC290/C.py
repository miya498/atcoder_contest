N,K = map(int,input().split())
A = list(map(int,input().split()))
A = list(set(A))
A.sort()

cnt = 0
for i in range(len(A)):
    if A[i] == cnt:
        cnt += 1
    else:
        break
ans = min(cnt,K)

print(ans)
