def popular_words(text: str, words: list) -> dict:

    lower_count = text.lower().split().count
    return {word: lower_count(word) for word in words}

    # text = text.lower().split()
    # dict_words = {}
    #
    # for word in words:
    #     count = 0
    #     if word in text:
    #         for w in text:
    #             if word == w:
    #                 count += 1
    #         dict_words[word] = count
    #     else:
    #         dict_words[word] = count
    #
    # return dict_words

# print(popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']))

if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
