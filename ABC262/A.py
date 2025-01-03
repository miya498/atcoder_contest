Y = int(input())

if Y%4 == 2:
    print(Y)
elif Y%4 == 3:
    ans = Y+(Y%4)
    print(ans)
else:
    ans = Y+(2-Y%4)
    print(ans)
