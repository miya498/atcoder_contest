x_1,y_1,x_2,y_2 = map(int,input().split())

for x in range(x_1-2,x_1+3):
    for y in range(y_1-2,y_1+3):
        ans_1 = (x-x_1)**2+(y-y_1)**2
        ans_2 = (x-x_2)**2+(y-y_2)**2
        if ans_1 == ans_2 == 5:
            print("Yes")
            exit()
print("No")
