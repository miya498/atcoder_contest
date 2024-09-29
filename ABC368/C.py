N = int(input())
H = list(map(int, input().split(' ')))

count = 0

for i in H:
    syou = i//5
    count += syou*3
    i -= syou*5
    while i>0:
        count += 1
        if count%3 == 0:
            i-=3
        else:
            i-=1

print(count)