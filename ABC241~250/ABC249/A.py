A,B,C,D,E,F,X = map(int,input().split())

Takahashi = (X//(A+C))*A*B
if X%(A+C) <= A:
    Takahashi += X%(A+C)*B
else:
    Takahashi += A*B

Aoki = (X//(D+F))*D*E

if X%(D+F) <= D:
    Aoki += X%(D+F)*E
else:
    Aoki += D*E

if Takahashi < Aoki:
    print("Aoki")
elif Takahashi == Aoki:
    print("Draw")
else:
    print("Takahashi")