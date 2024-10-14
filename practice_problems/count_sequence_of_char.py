def count_sequence(input_str: str) -> str:
    out = input_str[0]
    count = 1
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            out += str(count)
            out += input_str[i]
            count = 1
    out += str(count)
    return out


input_str = 'AABBBCCCD'

print(count_sequence(input_str))
output = 'A2B3C3D1'
