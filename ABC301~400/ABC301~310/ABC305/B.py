p,q = input().split()

A,B,C,D,E,F,G = 0,3,4,8,9,14,23
P = 0
Q = 0

if p == "A":
    P = A
elif p == "B":
    P = B
elif p == "C":
    P = C
elif p == "D":
    P = D
elif p == "E":
    P = E
elif p == "F":
    P = F
elif p == "G":
    P = G

if q == "A":
    Q = A
elif q == "B":
    Q = B
elif q == "C":
    Q = C
elif q == "D":
    Q = D
elif q == "E":
    Q = E
elif q == "F":
    Q = F
elif q == "G":
    Q = G

print(abs(P-Q))