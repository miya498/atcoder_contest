A, B = map(int,input().split())
socket = A
ans = 1

if B <= 1:
    print(0)
else:
    while True:
        if socket >= B:
            break
        socket += A-1
        ans += 1
    print(ans)
