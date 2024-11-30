N = int(input())
box = []
min_age = 1000000001
min_idx = 100
for i in range(N):
    s,a = input().split()
    if min_age > int(a):
        min_age = int(a)
        min_idx = i
    box.append(s)

ans = box[min_idx:]+box[:min_idx]

for i in range(N):
    print(ans[i])