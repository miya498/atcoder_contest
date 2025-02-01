X = int(input())
ans = 1
i = 1
while True:
    ans *= i
    i+=1
    if ans == X:
        print(i-1)
        exit()