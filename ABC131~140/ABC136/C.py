N = int(input())
H = list(map(int,input().split()))

for i in range(N-1):
    if H[i] <= H[i+1]:
        continue
    elif H[i] > H[i+1]:
        if H[i] - H[i+1] >= 2:
            print("No")
            exit()
        elif H[i] - H[i+1] == 1:
            H[i+1] = H[i]

print("Yes")
