A,B,C,D = map(int,input().split())

if A < C:
    print("Takahashi")
elif A == C:
    if B < D:
        print("Takahashi")
    elif B == D:
        print("Takahashi") 
    else:
        print("Aoki")
else:
    print("Aoki")    
