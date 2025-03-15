N = int(input())
A = list(map(int,input().split()))

cnt_1 = [0]*N
seen = set()
for i in range(N):
    seen.add(A[i])
    cnt_1[i] = len(seen)

cnt_2 = [0]*N
seen = set()

for i in range(N-1,-1,-1):
    seen.add(A[i])
    cnt_2[i] = len(seen)

ans = 0
for i in range(N-1):
    ans = max(ans,cnt_1[i]+cnt_2[i+1])

print(ans)


