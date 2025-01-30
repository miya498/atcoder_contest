num = int(input())
a = num//100
b = num%100//10
c = num%10

ans = (a+b+c)*111
print(ans)