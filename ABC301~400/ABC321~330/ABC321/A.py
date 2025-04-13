N = int(input())

D = []

while N > 0:
    num = N%10
    D.append(num)
    N //= 10

for i in range(1,len(D)):
    if D[i-1] >= D[i]:
        print("No")
        exit()
print("Yes")


