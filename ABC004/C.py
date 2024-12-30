N = int(input())

num = ["1","2","3","4","5","6"]

for i in range(N%30):
    x = num[i%5]
    num[i%5] = num[i%5+1]
    num[i%5+1] = x

print("".join(num)) 