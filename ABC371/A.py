a,b,c = input().split()

# ABC ACB BAC BCA CAB CBAの6パターン
#(BAC CAB)-> A (ABC CBA)->B (ACB BCA)->C
#<>> ><<  >>> <<< >>< <<>
if (a == "<" and b == ">" and c==">") or (a == ">" and b == "<" and c=="<"):
    print("A")
elif(a == ">" and b == ">" and c==">") or (a == "<" and b == "<" and c=="<"):
    print("B")
else:
    print("C")
