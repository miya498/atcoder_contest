N = int(input())
A = list(map(int,input().split()))

first = 0
first_index=-1
second = 0
ans = -1

for index, value in enumerate(A):
    if index==0:
        first=value
        first_index=index
        
    if first < value:
        second=first
        ans=first_index
        first = value
        first_index=index

    elif first > value and value >second:
        second = value
        ans = index

print(ans+1)