N = int(input())
T = input()

x = 0
y = 0
direction = "E"

for i in range(N):
    if T[i] == "S":

        if direction == "E":
            x += 1
        elif direction == "S":
            y -= 1
        elif direction == "W":
            x -= 1
        else:
            y += 1
    
    else:
        if direction == "E":
            direction = "S"
        elif direction == "S":
            direction = "W"
        elif direction == "W":
            direction = "N"
        else:
            direction = "E"

print(x,y)
