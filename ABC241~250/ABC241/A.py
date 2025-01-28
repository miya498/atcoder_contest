a,b,c,d,e,f,g,h,i,j = map(int,input().split())
num = [a,b,c,d,e,f,g,h,i,j]
ans = 0

for i in range(3):
    ans = num[ans]

print(ans)
