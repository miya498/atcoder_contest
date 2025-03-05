S = input()
cnt = 0

for num in range(10000):
    pin = str(num).zfill(4)
    valid = True

    for i in range(10):
        if S[i] == "o" and str(i) not in pin:
            valid = False
        if S[i] == "x" and str(i) in pin:
            valid = False
    if valid:
        cnt += 1
print(cnt)