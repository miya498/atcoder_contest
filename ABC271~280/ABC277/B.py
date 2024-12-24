N = int(input())

moji = set()
moji_1 = {"H", "D", "C", "S"}
moji_2 = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}
S = [input() for _ in range(N)]

for s in S:
    if len(s) != 2 or s[0] not in moji_1 or s[1] not in moji_2:
        print("No")
        exit()
    if s in moji:
        print("No")
        exit()
    moji.add(s)

print("Yes")