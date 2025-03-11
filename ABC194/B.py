N = int(input())
A,B = [],[]
ans = 1000000
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    ans = min(ans,a+b)

for i in range(N):
    for j in range(N):
        if i != j:
            ans = min(ans,max(A[i],B[j]))
print(ans)