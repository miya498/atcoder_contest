N,X,T = map(int,input().split())
if N%X == 0:
    cnt = N//X
else:
    cnt = N//X+1

print(T*cnt)