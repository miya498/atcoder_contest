N,R,C = map(int,input().split())
S = input()
smoke = {
    "N":(-1,0),
    "S":(1,0),
    "W":(0,-1),
    "E":(0,1)
}
x,y =0,0
seen = {(0,0)}
ans = ""
for i in range(N):
    dx,dy = smoke[S[i]]
    x += dx
    y += dy

    if ((x-R),(y-C)) in seen:
        ans += "1"
    else:
        ans += "0"
    seen.add((x,y))
print(ans)
