N = int(input())
S = input()

slash = [i for i, c in enumerate(S) if c == "/"]
ans = 0

for mid in slash:
    l = mid - 1
    r = mid + 1
    length = 1

    while l >= 0 and S[l] == "1" and r < N and S[r] == "2":
        length += 2
        l -= 1
        r += 1

    ans = max(ans, length)

print(ans)