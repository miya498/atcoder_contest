N,K = map(int,input().split())
R = list(map(int,input().split()))

ans = 0
R.sort()

for i in range(K):
    ans = (ans+R[i+N-K])/2

print(ans)