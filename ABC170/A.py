a,b,c,d,e = map(int,input().split())
num = [a,b,c,d,e]
for idx,i in enumerate(num):
    if i  == 0:
        print(idx+1)