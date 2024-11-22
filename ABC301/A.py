N = int(input())
S = input()

cnt_a = 0
cnt_t = 0

for i in range(N):
    if S[i] == "T":
        cnt_t += 1
    else:
        cnt_a += 1


if cnt_a < cnt_t:
    print("T")
elif cnt_a > cnt_t:
    print("A")
else:
    if S[-1] == "A":
        print("T")
    else:
        print("A")