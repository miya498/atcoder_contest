N,K = map(int,input().split())
A = list(map(int,input().split()))
a = [[num,i] for i,num in enumerate(A)]
a.sort()

ans = [K // N]*N
remaining = K%N
for i in range(remaining):
    ans[a[i][1]] += 1

print("\n".join(map(str,ans)))
