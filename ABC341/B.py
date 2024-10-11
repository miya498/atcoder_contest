N = int(input())
A = list(map(int,input().split()))

for i in range(N-1):
    s,t = map(int,input().split())
    cnt = A[i]//s
    A[i] = A[i]%s
    A[i+1] += cnt*t

print(A[N-1])