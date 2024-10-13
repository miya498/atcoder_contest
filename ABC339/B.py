H,W,N = map(int,input().split())

map_list = [["."]*W for __ in range(H)]

current_x = 0
current_y = 0
direct = "U" 

for i in range(N):
    if map_list[current_x][current_y] == ".":
        map_list[current_x][current_y] = "#"
        if direct == "U":
            direct = "R"
        elif direct == "R":
            direct = "D"
        elif direct == "D":
            direct = "L"
        else:
            direct = "U"
    else:
        map_list[current_x][current_y] = "."
        if direct == "U":
            direct = "L"
        elif direct == "L":
            direct = "D"
        elif direct == "D":
            direct = "R"
        else:
            direct = "U"
    
    if direct == "U":
        if current_x == 0:
            current_x = H-1
        else:
            current_x -= 1
    elif direct == "D":
        if current_x == H-1:
            current_x = 0
        else:
            current_x += 1
    elif direct == "L":
        if current_y == 0:
            current_y = W-1
        else:
            current_y -= 1
    elif direct == "R":
        if current_y == W-1:
            current_y = 0
        else:
            current_y += 1

for i in map_list:
    ans = "".join(i)
    print(ans)




    


