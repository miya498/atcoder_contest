N = list(map(int,input()))
k = len(N)
s = sum(N)
mod = s%3

if mod == 0:
    print(0)
    exit()

if k == 1:
    print(-1)
    exit()

if mod == 1:
    target = 2
else:
    target = 1

flag = False
cnt = 0
for num in N:
    if num%3 == mod:
        flag = True

    if num%3 == target:
        cnt += 1

if flag:
    print(1)
elif cnt >= 2 and k > 2:
    print(2)
else:
    print(-1)