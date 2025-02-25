def factorial(n):
    a = 1
    for i in range(1,n+1):
        a *= i
    return a
P = int(input())

i = 10
ans = 0
while i > 0:
    money = factorial(i)
    ans += P//money
    P = P%money
    i -= 1


print(ans)