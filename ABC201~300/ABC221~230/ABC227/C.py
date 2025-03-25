N = int(input())

ans = 0
for a in range(1,N+1):
    if a*a*a > N:
        break
    for b in range(a,N+1):
        if a*b*b > N:
            break
        max_c = N//a//b
        ans += max_c-b+1

print(ans)
