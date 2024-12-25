S = input()
T = input()

n = ["a","t","c","o","d","e","r","@"]
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    else:
        if S[i] == "@":
            if T[i] not in n:
                print("You will lose")
                exit()
        elif T[i] == "@":
            if S[i] not in n:
                print("You will lose")
                exit()
        else:
            print("You will lose")
            exit()

print("You can win")
             
