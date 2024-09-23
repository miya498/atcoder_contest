n,y = map(int,input().split())

for i in range(n+1):
    pool = False
    for j in range(n+1-i):
        cal = y - 10000*i - 5000*j

        if cal==1000*(n-i-j):
            print(i,j,n-i-j)
            pool = True
            break
    if pool:
        break

if pool != True:
    print("-1 -1 -1")