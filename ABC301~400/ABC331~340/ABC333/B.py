S = list(input())
T = list(input())

S.sort()
T.sort()

S_distance = ord(S[1])-ord(S[0])
T_distance = ord(T[1])-ord(T[0])

if S_distance > 2:
    S_distance = 5 - S_distance

if T_distance > 2:
    T_distance = 5 - T_distance

if S_distance == T_distance:
    print("Yes")
else:
    print("No")