Q = int(input())

stack = [0]*100

for _ in range(Q):
    query = input().split()

    if query[0] == "1":
        x = int(query[1])
        stack.append(x)
    else:
        print(stack.pop())
