A,B,C,K = map(int,input().split())
ans = 0
if K < A:
    print(K)
    exit()
else:
    ans = A
    K -= A

if K < B:
    print(ans)
    exit()
else:
    K = K-B

ans -= K
print(ans)