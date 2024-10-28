N = int(input())
A = list(map(int, input().split()))

indexed_A = {value: index+1 for index, value in enumerate(A)}
ans = []

person = indexed_A[-1]
ans.append(person)

for _ in range(N-1):
    person = indexed_A[person]
    ans.append(person)

print(*ans)