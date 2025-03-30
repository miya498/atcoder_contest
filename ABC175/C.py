X,K,D = map(int,input().split())

if X < 0:
    X *= -1

cnt = X//D
if K-cnt > 0:
    if (K-cnt)%2 == 0:
        ans = X - (cnt*D)
    else:
        cnt += 1
        ans = abs(X - (cnt*D))
else:
    ans = X-(K*D)
print(ans)
