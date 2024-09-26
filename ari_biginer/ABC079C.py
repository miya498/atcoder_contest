S = input()

for bit in range(8):
    total = int(S[0])
    for i in range(3):
        if bit & (1 << i):
            total += int(S[i+1])
        else:
            total -= int(S[i+1])
    if total == 7:
        for i in range(3):
            if bit & (1 << i):
                print(f"{S[i]}+",end="")
            else:
                print(f"{S[i]}-",end="")
        print(f"{S[3]}=7")
        break