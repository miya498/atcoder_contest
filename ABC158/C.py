A,B = map(int,input().split())

for i in range(1,1001):
    a = int(i*0.08)
    b = int(i*0.10)
    if a == A and b == B:
        print(i)
        exit()

print(-1)

