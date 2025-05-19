S = input()
S1 = int(S[:2])
S2 = int(S[2:])
flag1 = False
flag2 = False

if 1 <= S1 <= 12:
    flag1 = True
if 1 <= S2 <= 12:
    flag2 = True

if flag1 and flag2:
    print("AMBIGUOUS")
elif flag1:
    print("MMYY")
elif flag2:
    print("YYMM")
else:
    print("NA")

