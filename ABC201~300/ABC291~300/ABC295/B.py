R,C = map(int,input().split())
B = [list(input()) for _  in range(R)]

for i in range(R):
    for j in range(C):
        if B[i][j] != "." and B[i][j] != "#":
            move = int(B[i][j])
            for dx in range(-move,move+1):
                for dy in range(-move,move+1):
                    if 0 <= i+dx <= R-1 and 0 <= j+dy <= C-1:
                        if B[i+dx][j+dy] == "#" and abs(dx)+abs(dy) <= move:
                            B[i+dx][j+dy] = "."
            B[i][j] = "."     
             
for i in range(R):
    print("".join(B[i]))            