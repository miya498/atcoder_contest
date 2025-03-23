num = input()
N = len(num)
if N == 1:
    print("Yes")
    exit()
cnt = 0
while True:
    if num[N-cnt-1] == "0":
        cnt += 1
    else:
        break

string = "0"*cnt + num

if string == string[::-1]:
    print("Yes")
else:
    print("No")