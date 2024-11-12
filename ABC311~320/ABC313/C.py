N = int(input())

A = list(map(int,input().split()))

A.sort()
mean = sum(A)//N

B = [mean]*N

for i in range(sum(A)%N):
    B[N-1-i] += 1

ans = 0

for i in range(N):
    ans += abs(A[i]-B[i])

print(ans//2)
