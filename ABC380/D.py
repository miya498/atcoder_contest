def toggle_case(c):
    if 'a' <= c <= 'z':
        return chr(ord(c) - ord('a') + ord('A'))
    elif 'A' <= c <= 'Z':
        return chr(ord(c) - ord('A') + ord('a'))
    else:
        return c

def find_char(S, k):
    n = len(S)
    while k > n:
        k = (k - 1) % n + 1
    char = S[k - 1]
    return char

def main():
    S = input().strip()
    Q = int(input().strip())
    queries = [int(input().strip()) for _ in range(Q)]
    
    results = []
    for k in queries:
        char = find_char(S, k)
        results.append(char)
    
    print("".join(results))

if __name__ == "__main__":
    main()