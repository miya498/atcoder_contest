A,B,C,X = map(int,input().split())

if X <= A:
    print(1)
elif A+1 <= X <= B:
    ans = C/(B-A)
    print(ans)
else:
    print(0)