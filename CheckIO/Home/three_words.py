def checkio(words: str) -> bool:

    list_words = words.split()
    count = 0

    if len(list_words) == 0 or len(list_words) == 1:
        return False

    else:
        for i in list_words:
            if i.isalpha():
                count = count + 1
                if count >= 3:
                    return True
            else:
                count = 0
    return False



# print(checkio("Hi"))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
