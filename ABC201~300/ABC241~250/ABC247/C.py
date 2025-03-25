N = int(input())

ans = [1]

if N == 1:
    print(*ans)
    exit()

for i in range(2,N+1):
    ans = ans + [i] + ans 

print(*ans)