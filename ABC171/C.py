N = int(input())
ans = []

while N > 0:
    N -= 1
    ans.append(chr(N%26+ord("a")))
    N //= 26
ans.reverse()
print("".join(ans))
