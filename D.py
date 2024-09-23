from collections import deque

N = int(input())
H = list(map(int, input().split()))

result = deque()
count = 0

for i in range(N-1, -1, -1):
    if i == N-1:
        result.appendleft(count)
    elif i == N-2:
        count += 1
        result.appendleft(count)
    elif i >= 0:  
        if H[i] <= H[i+1]:  
            count += 1
        result.appendleft(count)

print(" ".join(map(str, result)))