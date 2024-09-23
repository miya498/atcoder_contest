def to_base_3(n):
    if n == 0:
        return '0'
    
    base_3 = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        base_3 = str(remainder) + base_3
    
    return base_3

def convert_to_format(base_3_str):
    digit_sum = sum(int(char) for char in base_3_str)
    
    digit_positions = []
    for position, digit in enumerate(reversed(base_3_str)):
        digit = int(digit)
        if digit > 0:
            for _ in range(digit):
                digit_positions.append(str(position))
    
    print(f"{digit_sum}")
    print(" ".join(digit_positions))

number = int(input())
base_3_str = to_base_3(number)
convert_to_format(base_3_str)
