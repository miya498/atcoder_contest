S = input()

cnt_f = 0
for i in range(len(S)):
    if S[i] == "a":
        cnt_f += 1
    else:
        break
cnt_b = 0
for i in range(1,len(S)+1):
    if S[-i] == "a":
        cnt_b += 1
    else:
        break

if cnt_f > cnt_b:
    print("No")
    exit()
s_add = "a"*(cnt_b-cnt_f) + S
n = len(s_add)
for i in range(len(s_add)):
    if s_add[i] != s_add[n-1-i]:
        print("No")
        exit()
print("Yes")