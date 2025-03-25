a,b,c,d = map(int,input().split())
if a > c:
    a,c =c,a
    b,d = d,b
b = abs(b)
d = abs(d)
ans = a+(c-a)*b/(d+b)
print(ans)