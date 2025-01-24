from collections import defaultdict

N = int(input())
X,Y = [],[]
y_set = set()
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
    y_set.add(y)

S = input()
state_R = defaultdict(list)
state_L = defaultdict(list)

for i in range(N):
    if S[i] == "L":
        state_L[Y[i]].append(X[i])
    else:
        state_R[Y[i]].append(X[i])


for y in y_set:
    if len(state_L[y]) >= 1 and len(state_R[y]) >= 1:
        if max(state_L[y]) > min(state_R[y]):
            print("Yes")
            exit()
print("No")
