S = input()
ans = 0
for i in range(len(S)):
    num = ord(S[i])-ord("A")+1
    ans += num*26**(len(S)-i-1)

print(ans)