N = int(input())

for k in range(1000):
    if N < 2**k:
        print(k-1)
        exit()