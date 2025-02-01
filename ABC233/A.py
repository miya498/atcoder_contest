X,Y = map(int,input().split())

if Y <= X:
    print(0)
    exit()
else:
    ans = (Y-X)//10
    if (Y-X)%10 != 0:
        ans += 1
print(ans)