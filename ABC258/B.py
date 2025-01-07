N = int(input())
A = [list(input()) for _ in range(N)]

def calc(x,y,h,w):
    result = ""
    for i in range(N):
        result += A[(x+h*i)%N][(y+w*i)%N]
    return int(result)

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans,calc(i,j,0,1))
        ans = max(ans,calc(i,j,1,0))
        ans = max(ans,calc(i,j,0,-1))
        ans = max(ans,calc(i,j,-1,0))
        ans = max(ans,calc(i,j,1,1))
        ans = max(ans,calc(i,j,-1,-1))
        ans = max(ans,calc(i,j,-1,1))
        ans = max(ans,calc(i,j,1,-1))

print(ans)
    
