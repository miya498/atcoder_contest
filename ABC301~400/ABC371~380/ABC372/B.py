M = int(input())
A = []
#1<=A<=10
for i in range(11):
    cal = M%3
    for j in range(cal):
        A.append(i)
    M //= 3
    if  M <= 2:
        for j in range(M):
            A.append(i+1)
        break

print(len(A))

for i in A:
    print(i,end=" ")
print()
    
#100->33...1 > 11...0 > 3...2 > 1...0
#10201