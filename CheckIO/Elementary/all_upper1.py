"""Check if a given string has all symbols in upper case. If the string is empty or
doesn't have any letter in it - function should return True.
Input: A string.
Output: a boolean.
Example:
is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == True
is_all_upper('444') == True
is_all_upper('55 55 5') == True"""

def is_all_upper(text: str) -> bool:
    return text == text.upper() if True else False
    # return False

print(is_all_upper('ALL UPPER'))
print(is_all_upper('all lower'))
print(is_all_upper(''))
print(is_all_upper('444'))
print(is_all_upper('55 55 5'))
