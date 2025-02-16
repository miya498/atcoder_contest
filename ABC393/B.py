S = input()

ans = 0
for i in range(len(S)-2):
    for j in range(1,len(S)):
        if i+j+j > len(S)-1:
            break
        if S[i] == "A" and S[i+j] == "B" and S[i+j+j] == "C":
            ans += 1

print(ans)