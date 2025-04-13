S = input() 

alph = {}
for idx, char in enumerate(S):
    alph[char] = idx

count = 0

for i in range(ord('A'), ord('Z')):
    current_char = chr(i)
    next_char = chr(i + 1)
    
    count += abs(alph[next_char] - alph[current_char])

print(count)
