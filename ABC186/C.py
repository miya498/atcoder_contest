N = int(input())
ans = 0
for i in range(1,N+1):
    i_10 = str(i)
    i_8 = oct(i)
    if "7" in i_10 or "7" in i_8:
        ans += 1
print(N-ans)