N = int(input())

S = []

for i in range(N):
    s = input()
    S.append(s)

flag = False
for i in range(N):
    for j in range(N):
        if i != j:
            gattai = S[i]+S[j]
            if gattai == gattai[::-1]:
                flag = True
                break

if flag:
    print("Yes")
else:
    print("No")