N,Y = map(int,input().split())

# 10000a+5000b+1000c=Y
# a+b+c=N -> c = N-a-bより
# 10000a+5000b+1000(N-a-b)=Y
# 1000N+9000a+4000b = Y

count = True
for i in range(N+1):
    for j in range(N+1-i):
        if 1000*N+9000*i+4000*j == Y:
            print(i,j,N-i-j)
            count = False
            break
    if count!=True:
        break

if count:
    print("-1 -1 -1")

