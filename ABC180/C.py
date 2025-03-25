import math 
N = int(input())
k = int(math.sqrt(N))
ans = []
for i in range(1,k+1):
    if N%i == 0:
        if N == i*i:
            ans.append(i)
        else:
            ans.append(i)
            ans.append(N//i)
ans.sort()
for a in ans:
    print(a)
