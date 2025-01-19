S = input()

flag = [True for _ in range(10)]

for i in range(9):
    flag[int(S[i])] = False

for i in range(10):
    if flag[i]:
        print(i)