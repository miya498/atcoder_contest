def dfs(current, n, m, results):
    if len(current) == n:
        results.append(current[:])
        return
    start = current[-1] + 10 if current else 1
    for next_val in range(start, m + 1):
        current.append(next_val)
        dfs(current, n, m, results)
        current.pop()

N, M = map(int, input().split())
results = []
dfs([], N, M, results)

print(len(results))
for result in results:
    print(*result)