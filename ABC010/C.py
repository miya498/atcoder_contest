import math

txa,tya,txb,tyb,T,V =map(int,input().split())
n = int(input())
flag = False
idoukyori = T*V

for _ in range(n):
    x,y = map(int,input().split())
    uwaki = math.sqrt((x-txa)**2+(y-tya)**2)+math.sqrt((x-txb)**2+(y-tyb)**2)
    if idoukyori >= uwaki:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
