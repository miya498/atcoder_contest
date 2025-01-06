def run_length_encoding(s):
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append((s[i - 1], count))
            count = 1
    encoded.append((s[-1], count))
    return encoded

S = input()
T = input()

compressed_S = run_length_encoding(S)
compressed_T = run_length_encoding(T)

if len(compressed_S) != len(compressed_T):
    print("No")
    exit()

for (char_S, count_S), (char_T, count_T) in zip(compressed_S, compressed_T):
    if char_S != char_T or count_S > count_T or (count_S == 1 and count_T > 1):
        print("No")
        exit()

print("Yes")