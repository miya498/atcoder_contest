N = int(input())
H = list(map(int,input().split()))

max_idx = -1
maxsize = 0

for i in range(N):
    if H[i] > maxsize:
        maxsize = H[i]
        max_idx = i+1

print(max_idx)