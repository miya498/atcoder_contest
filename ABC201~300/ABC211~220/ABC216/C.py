N = int(input())
operations = []

while N > 0:
    if N % 2 == 0:
        operations.append("B")
        N //= 2
    else:
        operations.append("A")
        N -= 1
operations.reverse()
print("".join(operations))