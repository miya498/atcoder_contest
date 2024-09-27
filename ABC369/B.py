N = int(input())

left = 0
right = 0
ans = 0

for i in range(N):
    A, S = input().split()
    A = int(A)

    if S == "L":
        if left == 0:
            left = A
        else:
            ans += abs(A-left)
            left = A
    else:
        if right == 0:
            right = A
        else:
            ans += abs(A-right)
            right = A    

print(ans)        

