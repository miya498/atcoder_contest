from itertools import permutations

def in_palindrome(s):
    for now in range(n - k + 1):
        if all(s[now + i] == s[now + k - i - 1]for i in range(k // 2)):
            return True
    return False


n, k = map(int, input().split())
s = input()
check = set()
ans = 0
for p in permutations(s):
    if p in check:
        continue
    check.add(p)
    if not in_palindrome(p):
        ans += 1

print(ans)