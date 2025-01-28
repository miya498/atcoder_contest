x_1,y_1 = map(int,input().split())
x_2,y_2 = map(int,input().split())
x_3,y_3 = map(int,input().split())

ans = []
if x_1 == x_2:
    ans.append(x_3)
elif x_2 == x_3:
    ans.append(x_1)
elif x_1 == x_3:
    ans.append(x_2)

if y_1 == y_2:
    ans.append(y_3)
elif y_2 == y_3:
    ans.append(y_1)
elif y_1 == y_3:
    ans.append(y_2)

print(*ans)