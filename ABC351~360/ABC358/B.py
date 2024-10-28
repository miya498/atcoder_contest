N,A = map(int,input().split())
T = list(map(int,input().split()))
ans = 0

for i in range(N):
    if i == 0:
        ans += T[i]+A
        print(ans)
    else:
        if ans > T[i]:
            print(ans+A)
            ans += A
        else:
            print(T[i]+A) 
            ans = T[i]+A