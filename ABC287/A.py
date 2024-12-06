N = int(input())
cnt = 0
for i in range(N):
    s = input()
    if s == "For":
        cnt += 1

if cnt >= (N+1)//2:
    print("Yes")
else:
    print("No")