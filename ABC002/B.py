W = input()

ans = ""
moji = ["a","i","u","e","o"]
for s in W:
    if s not in moji:
        ans += s

print(ans)           
