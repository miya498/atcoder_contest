S = list(input())

cnt_low = 0
for i in range(len(S)):
    if 97 <= ord(S[i]) and ord(S[i]) <= 122:
        cnt_low += 1

cnt_high = len(S)-cnt_low

ans = "".join(S)
if cnt_high > cnt_low:
    ans=ans.upper()
else:
    ans=ans.lower()

print(ans)
    