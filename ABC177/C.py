N = int(input())
A = list(map(int,input().split()))
ans = sum(A)*sum(A)
for i in range(N):
    ans -= A[i]**2

print((ans//2)%(1000000000+7))