N = int(input())

W = list(input().split())

word = ["and","not","that","the","you"]

for i in range(N):
    if W[i] in word:
        print("Yes")
        exit()

print("No")