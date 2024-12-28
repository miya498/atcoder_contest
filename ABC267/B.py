S=list(input())
R1=[S[6]]
R2=[S[3]]
R3=[S[1],S[7]]
R4=[S[0],S[4]]
R5=[S[2],S[8]]
R6=[S[5]]
R7=[S[9]]
R=""
if "1" in R1:
    R+="o"
else:
    R+="x"
if "1" in R2:
    R+="o"
else:
    R+="x"
if "1" in R3:
    R+="o"
else:
    R+="x"
if "1" in R4:
    R+="o"
else:
    R+="x"
if "1" in R5:
    R+="o"
else:
    R+="x"
if "1" in R6:
    R+="o"
else:
    R+="x"
if "1" in R7:
    R+="o"
else:
    R+="x"

if S[0]=="0" and ("oxo" in R or "oxxo" in R or "oxxxo" in R or "oxxxxo" in R or "oxxxxxo" in R):
    print("Yes")
else:
    print("No")