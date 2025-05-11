L,R = map(int,input().split())

if R-L >= 2019:
    print(0)
else:
    n = R//2019
    if L <= n*2019:
        print(0)
    else:
        ans = float("inf")
        n = min(R,L+2019)
        for i in range(L,n):
            for j in range(i+1,n+1):
                ans = min(ans,i*j%2019)
        print(ans)
