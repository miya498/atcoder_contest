X = int(input())
cnt = X //500
ans = cnt*1000
X = X % 500
cnt = X //5
ans += cnt*5

print(ans)
