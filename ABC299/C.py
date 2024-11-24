N = int(input())
S = input()

if '-' not in S or 'o' not in S:
    print(-1)
    exit()

dango = S.split("-")

ans = max(len(segment) for segment in dango if segment)
print(ans)