a,b,c,d,e,f = map(int,input().split())

ans = abs((e-a)*(d-b)-(c-a)*(f-b))/2

print(ans)