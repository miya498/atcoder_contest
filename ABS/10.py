S = input()

divide = ["dream","dreamer","erase","eraser"]

S = S[::-1]

reverse_divide = [word[::-1] for word in divide]

can = True
i = 0
while i < len(S):
    found = False
    for word in reverse_divide:
        if S[i:i+len(word)] == word:
            found = True
            i += len(word)
            break
    if not found:
        can = False
        break

if can:
    print("YES")
else:
    print("NO")
