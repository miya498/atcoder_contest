N,A,B = map(int,input().split())
cnt = N//(A+B)
if N%(A+B) >= A:
    print(cnt*A + A)
else:
    print(cnt*A + N%(A+B))

