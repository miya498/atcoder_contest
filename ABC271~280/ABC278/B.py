def hantei(h,m):
    return 0<=h<=23 and 0<=m<=59

def misjudge(h,m):
    a,b = h//10,h%10
    c,d = m//10,m%10
    AC = a*10+c
    BD = b*10+d
    return hantei(AC,BD)

H,M = map(int,input().split())

while not misjudge(H,M):
    M += 1
    if M == 60:
        H,M = H+1,0
    if H == 24:
        H = 0

print(H,M)