n = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(n):
    flower = A[i]%6
    if flower > 3:
        ans += flower-3
    elif flower==1 or flower ==3:
        ans += 0
    elif flower == 0:
        ans += 3
    else:
        ans += 1
print(ans)