def is_palindrome(s):
    return s == s[::-1]

S = input()
N = len(S)
T = S[:(N-1)//2]
U = S[(N+3)//2-1:]

if is_palindrome(S) and is_palindrome(T) and is_palindrome(U):
    print("Yes")
else:
    print("No")
