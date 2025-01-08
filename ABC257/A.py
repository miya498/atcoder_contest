N,X = map(int,input().split())
S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string = ""
for i in range(26):
    string += S[i]*N
print(string[X-1])