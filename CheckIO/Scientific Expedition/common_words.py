def checkio(line1: str, line2: str) -> str:

    text1 = line1.split(',')
    text2 = line2.split(',')
    result = []

    for letter1 in text1:
        if letter1.isalpha() and letter1 in text2:
            result.append(letter1)
    result = sorted(result)
    return str(','.join(result))


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
