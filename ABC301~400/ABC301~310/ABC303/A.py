N = int(input())
S = input()
T = input()

def similar(x, y):
    if x == y:
        return True
    if (x == '1' and y == 'l') or (x == 'l' and y == '1'):
        return True
    if (x == '0' and y == 'o') or (x == 'o' and y == '0'):
        return True
    return False

for i in range(N):
    if not similar(S[i], T[i]):
        print("No")
        exit()

print("Yes")