K = int(input())
cnt = []

while K != 1:
    y = K%2
    cnt.append(y)
    K = K//2
cnt.append(1)
cnt.reverse()

ans = ""
for i in range(len(cnt)):
    if cnt[i] == 1:
        ans += "2"
    else:
        ans += "0"

print(ans)