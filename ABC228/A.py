S,T,X = map(int,input().split())

if S < T:
    if S <= X < T:
        print("Yes")
        exit()
else:
    if X < T or S <= X:
        print("Yes")
        exit()
print("No")