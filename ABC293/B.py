N = int(input())
A = list(map(int,input().split()))
B = [False]*N

ans = []

for i in range(N):
    if B[i] == False:
        B[A[i]-1] = True

for i in range(N):
    if B[i] == False:
        ans.append(i+1)

print(len(ans))
print(*ans)
