N = int(input())
L = list(map(int,input().split()))
ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if L[i] != L[j] and L[j]!= L[k] and L[i]!=L[k] and L[i]+L[j] > L[k] and L[i]+L[k] > L[j]  and L[k]+L[j] > L[i]:
                ans += 1
print(ans)