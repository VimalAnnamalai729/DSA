def valid_parenthesis(s: str) -> bool:
    open_braces = {'{': '}', '(': ')', '[': ']'}
    waiting_brac_index = []
    result = True
    for i, bracket in enumerate(s):
        if i in waiting_brac_index:
            continue
        val = s.find(open_braces.get(bracket), i) if bracket in open_braces else -1

        if val != -1 and i % 2 == 0 and val % 2 == 1:
            waiting_brac_index.append(val)
            continue
        elif i % 2 == 1 and val % 2 == 0:
            waiting_brac_index.append(val)
            continue
        else:
            result = False
    return result


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
