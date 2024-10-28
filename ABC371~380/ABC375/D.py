S = list(input())
count = 0

for i in range(len(S)-2):
    for k in range(i+2, len(S)):
        if S[i] == S[k]:
            count += k-i-1

print(count)