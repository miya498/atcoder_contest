from collections import deque

N = int(input())
A = list(map(int,input().split()))
A.sort()
q = deque(A)

ans = 0
while q:
    if ans+1 == q[0]:
        q.popleft()
        ans += 1
    else:
        if len(q) >= 2:
            q.pop()
            q.pop()
            ans += 1
        else:
            break
    
print(ans)