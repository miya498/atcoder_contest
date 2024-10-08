S = list(input())
 
if S[0] != S[1] and S[0] != S[2]:
    print(1)
    exit()

check = S[0]

for i in range(1,len(S)):
    if check != S[i]:
        print(i+1)
        break
    
