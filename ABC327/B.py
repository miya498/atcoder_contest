B = int(input())

for i in range(1,100001):
    if B == i**i:
        print(i)
        break
    if i**i > B:
        print(-1)
        break