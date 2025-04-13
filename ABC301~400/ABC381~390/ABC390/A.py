a,b,c,d,e = map(int,input().split())
A = [a,b,c,d,e]

ans = [[2,1,3,4,5],[1,3,2,4,5],[1,2,4,3,5],[1,2,3,5,4]]

if A in ans:
    print("Yes")
else:
    print("No")