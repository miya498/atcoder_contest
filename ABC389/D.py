R = int(input())  

cnt = 0
h = R+2

for i in range(R+1):
    while h>0 and (h+0.5)**2+(i+0.5)**2>R**2:
        h -= 1
    cnt += h


print(cnt*4+1)