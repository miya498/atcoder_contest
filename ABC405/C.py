N = int(input())
A = list(map(int,input().split()))

ans = sum(A)*sum(A)

for i in range(N):
    ans -= A[i]*A[i]

print(ans//2)
