N = int(input())

for i in range(N,920):
    number = list(str(i))
    if int(number[0])*int(number[1]) == int(number[2]):
        print(i)
        break