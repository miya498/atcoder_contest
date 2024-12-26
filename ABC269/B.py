grid = [input() for _ in range(10)]

flag = True
for i in range(10):
    for j in range(10):
        if grid[i][j] == "#" and flag:
            A = i+1
            C = j+1
            B = i+1
            D = j+1
            flag = False
        elif grid[i][j] == "#":
            B = i+1
            D = j+1

print(A,B)
print(C,D)
