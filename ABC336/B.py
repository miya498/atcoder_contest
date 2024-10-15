N = int(input())

result = list(bin(N))
ans = 0
n = len(result)
for i in range(n):
    if result[n-1-i] == "1":
        break
    else:
        ans += 1

print(ans)