import re
def find_message(message: str) -> str:

    return ''.join(re.findall('[A-Z^]', message))


#   '_'.join(re.findall('([A-Z][^A-Z]*)', name)).lower()

# print(find_message('How are you? Eh, ok. Low or Lower? '
#  + 'Ohhh.'))

if __name__ == '__main__':
    print("Example:")
    print(find_message(('How are you? Eh, ok. Low or Lower? '
 + 'Ohhh.')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_message(('How are you? Eh, ok. Low or Lower? '
 + 'Ohhh.')) == 'HELLO'
    assert find_message('hello world!') == ''
    assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
    print("Coding complete? Click 'Check' to earn cool rewards!")
