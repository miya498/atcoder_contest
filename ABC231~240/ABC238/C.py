N = int(input())

n = str(N)
keta = len(n)
ans = 0
for i in range(keta):
    if i == keta-1:
        ans += (1+(N-10**i+1))*(N-10**i+1)//2
    else:
        ans += (1+(9*10**i))*(9*10**i)//2
print(ans%998244353)