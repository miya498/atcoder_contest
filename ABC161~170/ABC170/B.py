X,Y = map(int,input().split())

for x in range(X+1):
    if 2*x+4*(X-x) == Y:
        print("Yes")
        exit()
print("No")