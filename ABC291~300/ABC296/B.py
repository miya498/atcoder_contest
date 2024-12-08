S = [input() for _ in range(8)]

x = [1,2,3,4,5,6,7,8]
y = ["a","b","c","d","e","f","g","h"]
for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            ans = y[j]+str(8-i)
            print(ans)
