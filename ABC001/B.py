m = int(input())

if m < 100:
    print("00")
elif 100 <= m and m <= 5000:
    m *= 10
    ans = m//1000
    ans = str(ans)
    print(ans.zfill(2))

elif 6000 <= m and m <= 30000:
    ans = m//1000
    print(ans+50)
elif 35000 <= m and m <= 70000:
    ans = (m-30000)//5000 + 80
    print(ans)
else:
    print(89)