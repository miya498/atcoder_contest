S = input()
ans = 0
i =0 

while i<len(S):
    if S[i] == "0":
        if i+1 < len(S) and S[i+1] == "0":
            ans += 1
            i += 2
        else:
            ans +=1
            i += 1
    else:
        i+= 1
        ans += 1
print(ans)
