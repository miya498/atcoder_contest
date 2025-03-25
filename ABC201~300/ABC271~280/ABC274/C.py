N = int(input())
A = [0]+list(map(int,input().split()))

ans = [0]*(N*2+2)

for i in range(1,N+1):
    ans[2*i] = ans[A[i]] + 1
    ans[2*i+1] = ans[A[i]] + 1
for i in range(1,2*N+2):
    print(ans[i])