N = int(input())

div = N//5
a = div*5
b = (div+1)*5

if (N-a) < (b-N):
    print(a)
else:
    print(b)

