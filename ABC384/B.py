N,R = map(int,input().split())

for i in range(N):
    d,a = map(int,input().split())
    if d == 1:
        if 1600 <= R <= 2799:
            R += a
    if d == 2:
        if 1200 <= R <= 2399:
            R += a

print(R)
