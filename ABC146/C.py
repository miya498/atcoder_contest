A,B,X = map(int,input().split())

if A+B > X:
    print(0)
    exit()

left = 0
right = 10**9+1

while right - left > 1:
    mid = (left + right) // 2
    if A*mid + B*len(str(mid)) <= X:
        left = mid
    else:
        right = mid

print(left)
