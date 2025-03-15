S = input()
j = 0

for c in S:
    while True:
        if j%2 == 0:
            cha = "i"
        else:
            cha = "o"

        if c == cha:
            j += 1
            break
        else:
            j += 1
if j%2 != 0:
    j += 1
print(j-len(S))
