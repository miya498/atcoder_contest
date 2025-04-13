N = int(input())

ans = True
hozon = "yaha"
for i in range(N):
    s = input()
    if s == "sweet":
        if i != N-1 and s == hozon:
            ans = False
    hozon = s

if ans:
    print("Yes")
else:
    print("No")