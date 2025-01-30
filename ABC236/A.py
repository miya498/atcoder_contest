S = input()
a,b = map(int,input().split())

S_list = list(S)
S_list[a-1], S_list[b-1] = S_list[b-1], S_list[a-1]
ans = "".join(S_list)
print(ans)
