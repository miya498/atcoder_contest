N = int(input())
print(1)

num = [i for i in range(2,2*N+2)]
while len(num) != 0:
    s = int(input())
    num.remove(s)
    print(num[0])
    num.pop(0)