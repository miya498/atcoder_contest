N = int(input())
ans = 10**12
for i in range(1,10**6+1):
    if N%i == 0:
        j = N//i
        ans = min(ans,i+j-2)

print(ans)