A,B,C,D = map(int,input().split())

if C*D-B <= 0:
    print(-1)
    exit()

ans = 0
blue = A
red = 0
while red*D < blue:
    blue += B
    red += C
    ans += 1

print(ans)