P = list(map(int,input().split()))

ans = ""

for i in P:
    s = ord("a")+i-1
    ans += chr(s)

print(ans)