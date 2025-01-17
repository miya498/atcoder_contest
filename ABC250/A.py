H,W = map(int,input().split())
R,C = map(int,input().split())

hen = [(0,1),(1,0),(-1,0),(0,-1)]

ans = 0
for dx,dy in hen:
    if 1 <= R+dx <= H and  1 <= C+dy <= W:
        ans += 1

print(ans)