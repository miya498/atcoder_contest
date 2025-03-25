N = int(input())
S = input()
W = list(map(int, input().split()))

# 体重の情報を (体重, 本来の属性) のペアにしてリスト化
people = [(W[i], int(S[i])) for i in range(N)]

people.sort(key=lambda x: (x[0],x[1]))

correct = sum(1 for _, attr in people if attr == 1)
max_correct = correct

# 境界値ごとに正答数を計算
for i in range(N):
    if people[i][1] == 0:
        correct += 1
    else:
        correct -= 1
    
    if i == N-1 or people[i][0] != people[i+1][0]:
        max_correct = max(correct,max_correct)

print(max_correct)