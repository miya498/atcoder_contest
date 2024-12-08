from collections import Counter

N = int(input())
A = list(map(int,input().split()))

C = Counter(A)

ans = 0
for i in C.values():
    ans += i//2
    
print(ans)