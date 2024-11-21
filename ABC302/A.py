A,B = map(int,input().split())

ans = A//B

if A%B != 0:
    print(ans+1)
else:
    print(ans)