N = int(input())

flag = True

while N >= 2:
    if N%2 != 0:
        while N >= 2:
            if N%3 != 0:
                flag = False
                break
            else:
                N = N//3
        break
    else:
        N = N//2

if flag:
    print("Yes")
else:
    print("No") 