def between_markers(text: str, begin: str, end: str) -> str:

    # begin = text.find(begin)
    # end = text.find(end)
    # print(begin, end)
    return text[text.find(begin)+1:text.find(end)]
# print(between_markers('What is >apple<', '>', '<'))

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
