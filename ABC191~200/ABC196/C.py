N = int(input())
ans = 0

for i in range(1,1000000):
    num = str(i)+str(i)
    num = int(num)
    if num <= N:
        ans += 1
    else:
        break

print(ans)