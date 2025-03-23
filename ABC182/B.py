N = int(input())
A = list(map(int,input().split()))
max_A = max(A)
ans = 0
max_gcd = 0
for k in range(2,max_A+1):
    gcd = 0
    for a in A:
        if a % k == 0:
            gcd += 1
    if max_gcd < gcd:
        max_gcd = gcd
        ans = k
print(ans)
