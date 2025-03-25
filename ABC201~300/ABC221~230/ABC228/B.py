N,X = map(int,input().split())
A = list(map(int,input().split()))
ans = [0]*N

ans[X-1] = 1
to_f = A[X-1]
while True:
    if ans[to_f-1] != 1:
        ans[to_f-1] = 1
    else:
        break
    to_f = A[to_f-1]
print(sum(ans))


