N = int(input())

ans = int(N*1.08)

if ans < 206:
    print("Yay!")
elif ans == 206:
    print("so-so")
else:
    print(":(")