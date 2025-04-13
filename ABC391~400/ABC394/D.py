S = input()
st = []
p = {")": "(", "]": "[", ">": "<"}

for c in S:
    if c in "([<":
        st.append(c)
    elif st and st[-1] == p.get(c, ""):
        st.pop()
    else:
        print("No")
        exit()

if not st:
    print("Yes")
else:
    print("No")