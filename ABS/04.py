N = int(input())
A = list(map(int, input().split()))

count = 0
while True:
    if all(x%2 == 0 for x in A):
        count += 1
        A = [x//2 for x in A]
    else:
        break

print(count)