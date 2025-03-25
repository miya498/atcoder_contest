S = list(input())
if len(set(S)) == 1:
    print(-1)
elif S[0] == S[1]:
    print(S[2])
elif S[0] == S[2]:
    print(S[1])
elif S[1] == S[2]:
    print(S[0])
else:
    print(S[0])
         
