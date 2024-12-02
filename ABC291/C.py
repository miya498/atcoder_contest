N = int(input())
S = input()
zahyou = set()

x, y = 0, 0
zahyou.add((x, y))

for i in range(N):
    if S[i] == "R":
        x += 1
    elif S[i] == "L":
        x -= 1
    elif S[i] == "U":
        y += 1
    else:
        y -= 1

    if (x, y) in zahyou:
        print("Yes")
        exit()

    zahyou.add((x, y))

print("No")
