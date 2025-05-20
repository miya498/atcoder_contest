N = int(input())
restaurant = []
for i in range(N):
    s,p = input().split()
    restaurant.append((s,int(p),i+1))

restaurant.sort(key=lambda x: (x[0],-x[1]))

for i in range(N):
    print(restaurant[i][2])

