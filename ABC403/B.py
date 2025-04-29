T = input()
U = input()

ans = False
for i in range(len(T)-len(U)+1):
    flag = True
    for j in range(len(U)):
        if T[i+j] != U[j] and T[i+j] != "?":
            flag = False
            break
    if flag:
        ans = True
        break
print("Yes" if flag else "No")
