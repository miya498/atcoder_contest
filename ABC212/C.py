N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()


i = 0
j = 0
ans = abs(A[i]-B[i])
while i < N-1 and j < M-1:
    if abs(A[i+1]-B[j]) < abs(A[i]-B[j+1]):
        ans = min(abs(A[i+1]-B[j]),ans)
        i += 1
    else:
        ans = min(abs(A[i]-B[j+1]),ans)
        j += 1

print(ans)