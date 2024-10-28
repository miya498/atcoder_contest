a,b,c,d,e,f = map(int,input().split())
g,h,i,j,k,l = map(int,input().split())

def check(l_x1,r_x1,l_x2,r_x2):
    if l_x1 >= r_x2 or r_x1 <= l_x2:
        return False
    else:
        return True

if check(a,d,g,j) and check(b,e,h,k) and check(c,f,i,l):
    print("Yes")
else:
    print("No")