import math
X = int(input())
money = 100
ans = 0
while money < X:
    money = math.floor(money*101//100)
    ans += 1
print(ans)