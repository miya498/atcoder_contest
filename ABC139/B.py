A, B = map(int,input().split())

for i in range(20):
    count = A+(A-1)*(i-1)
    if count >= B:
        print(i)
        break