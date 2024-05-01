N, Q= map(int, input().split())
ans = [1]*N
yaha = list(map(int, input().split()))
for i in range(Q):
    dict=yaha[i]-1
    if ans[dict]==0:
        ans[dict]=1
    elif ans[dict]:
        ans[dict]=0

print(sum(ans))