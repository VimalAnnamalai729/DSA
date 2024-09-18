# Optimized Solution
def is_valid(s: str) -> bool:
    braces = {'}': '{', ')': '(', ']': '['}
    parsed_bracket = []

    for bracket in s:
        if bracket in braces.values():
            parsed_bracket.append(bracket)
        elif not parsed_bracket or braces[bracket] != parsed_bracket.pop():
            return False

    return not parsed_bracket


print(is_valid('()') == True)
print(is_valid('(){}') == True)
print(is_valid('(}') == False)
print(is_valid('(){}}{') == False)
print(is_valid('[[[]') == False)
print(is_valid("[({])}") == False)
