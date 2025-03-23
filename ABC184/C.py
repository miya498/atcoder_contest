r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

dx = abs(r1 - r2)
dy = abs(c1 - c2)

if r1 == r2 and c1 == c2:
    print(0)
elif dx + dy <= 3 or r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
    print(1)
elif dx + dy <= 6 or abs(dx - dy) <= 3 or (dx + dy) % 2 == 0:
    print(2)
else:
    print(3)
